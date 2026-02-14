import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import google.generativeai as genai
import json
import tools

# API KEY: Check env vars, otherwise prompt user.
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("[-] GOOGLE_API_KEY not found in environment variables.")
    try:
        GOOGLE_API_KEY = input("[?] Please paste your Google API Key here and press Enter: ").strip()
    except EOFError:
        print("[!] Input failed (EOF). Are you running this in a non-interactive console?")

if not GOOGLE_API_KEY:
    print("[!] No API Key provided. Agent will not function.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)
    try:
        # Dynamically find a supported model
        print("[*] Checking available models...")
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        target_model = "models/gemini-1.5-flash"
        
        if target_model in available_models:
            print(f"[+] Found optimized model: {target_model}")
            model_name = target_model
        elif "models/gemini-pro" in available_models:
            print("[!] Gemini 1.5 Flash not found. Falling back to Gemini Pro.")
            model_name = "models/gemini-pro"
        elif available_models:
            model_name = available_models[0]
            print(f"[!] Target models not found. Auto-selected: {model_name}")
        else:
            raise Exception("No models found that support 'generateContent'. Check your API Key permissions.")

        # Test the key immediately
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello")
        print("[+] API Key and Model verified successfully!")
        
        # Store model name for Agent class to use later
        os.environ["USED_MODEL_NAME"] = model_name
        
    except Exception as e:
        print(f"[-] API Key verification FAILED: {e}")
        print("[-] Please check your key or run 'fix_and_run.bat' to update libraries.")

app = FastAPI(title="CyberGuardian Analysis Agent")

# --- Agent System Prompt ---
SYSTEM_PROMPT = """
You are CyberGuardian, an advanced Cybersecurity AI Agent.
Your goal is to assist security professionals by analyzing risks, checking threat intelligence, and monitoring systems.

You have access to the following tools:

1. calculate_risk_score(open_ports: int, critical_vulns: int, server_importance_score: int) -> dict
   - Use this when the user wants to assess the risk of a server or asset.
   
2. check_threat_intel(domain: str) -> dict
   - Use this to check if a domain is malicious or suspicious.

3. monitor_logs(target_event: str, threshold: int) -> dict
   - Use this to watch for specific log events (like 'failed_login') and alert if they exceed a count.

CRITICAL RULES:
1. SINGLE TASK ONLY: You must only perform the ONE task requested.
2. STOP IMMEDIATELY: As soon as you get a result from a tool (like calculate_risk_score), summarize it and STOP.
3. NO HALLUCINATIONS: Do not "check logs", "monitor events", or "verify domains" unless EXPLICITLY asked.
4. If the user asks for a calculation, just do the calculation. Do not add extra security checks.

RESPONSE FORMAT:
- If you need to use a tool, return raw JSON: {"tool": "tool_name", "params": {...}}
- If you have the tool result, DO NOT call another tool. Formulate your final answer immediately.
- Final answer should be natural language summarizing the findings.
"""

# --- Message Models ---
class ChatRequest(BaseModel):
    message: str
    history: List[Dict[str, str]] = []

class ChatResponse(BaseModel):
    response: str
    logs: List[str] # To show the "Agentic" thought process

# --- Agent Logic ---
class Agent:
    def __init__(self):
        self.model = None
        if GOOGLE_API_KEY:
             model_name = os.environ.get("USED_MODEL_NAME", "gemini-1.5-flash")
             self.model = genai.GenerativeModel(model_name)

    def execute_tool(self, tool_name, params):
        if tool_name == "calculate_risk_score":
            return tools.calculate_risk_score(**params)
        elif tool_name == "check_threat_intel":
            return tools.check_threat_intel(**params)
        elif tool_name == "monitor_logs":
            return tools.monitor_logs(**params)
        else:
            return {"error": f"Unknown tool: {tool_name}"}

    async def run(self, user_query: str):
        logs = []
        conversation = f"{SYSTEM_PROMPT}\n\nUser Query: {user_query}\n"
        
        # Max steps to prevent infinite loops
        for step in range(5):
            logs.append(f"Step {step+1}: Thinking...")
            
            # 1. Calls LLM
            if not self.model:
                return "Error: GOOGLE_API_KEY not found. Please set it in your environment.", logs
            
            response = self.model.generate_content(conversation)
            text_response = response.text.strip()
            
            logs.append(f"Model Output: {text_response}")
            
            # 2. Check if it's a tool call (JSON)
            if text_response.startswith("{") and "tool" in text_response:
                try:
                    tool_data = json.loads(text_response)
                    tool_name = tool_data.get("tool")
                    params = tool_data.get("params", {})
                    
                    logs.append(f"ACTION: Calling {tool_name} with {params}")
                    
                    # 3. Execute Tool
                    result = self.execute_tool(tool_name, params)
                    result_str = json.dumps(result)
                    
                    logs.append(f"OBSERVATION: Tool returned {result_str}")
                    
                    # 4. Feed back to LLM
                    conversation += f"\nAssistant: {text_response}\nSystem: Tool Result: {result_str}\n"
                    conversation += "SYSTEM INSTRUCTION: Verify if this result answers the user's question. If yes, generate the Final Answer immediately. DO NOT call any more tools."
                    
                except Exception as e:
                    logs.append(f"Error parsing/executing tool: {e}")
                    conversation += f"\nSystem: Error executing tool: {e}\n"
            else:
                # Final response
                return text_response, logs
        
        return "Agent timed out or got stuck in a loop.", logs

agent_instance = Agent()

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response_text, agent_logs = await agent_instance.run(request.message)
        return ChatResponse(response=response_text, logs=agent_logs)
    except Exception as e:
        import traceback
        traceback.print_exc() # Print to terminal
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    print("Starting CyberGuardian Backend...")
    uvicorn.run(app, host="127.0.0.1", port=8080)
