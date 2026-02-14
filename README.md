CyberGuardian: AI-Powered Security Analyst Agent
CyberGuardian is a browser-based AI Agent that assists Security Operations Center (SOC) analysts by automating routine triage tasks. It connects a Chrome Extension frontend to a local Python backend powered by Google Gemini 1.5 Flash.

1. Introduction
Modern SOC analysts are overwhelmed by alerts and data. Shifting context between SIEMs, Threat Intel platforms, and calculators slows down response times. CyberGuardian acts as an intelligent sidekick, living in your browser, ready to perform risk calculations, check threat intelligence, and monitor logs autonomously using Agentic AI workflows.

2. The Problem
Tool Fatigue: Analysts switch between 10+ tabs to triage one alert.
Alert Overload: High volume of low-fidelity alerts leads to burnout.
Manual Calculations: Risk scoring (e.g., CVSS + Asset Value) is often done manually or in spreadsheets.
Static Automation: Traditional scripts break when inputs change; they lack reasoning capabilities.
3. The Solution
CyberGuardian uses an Agentic Loop (Reasoning + Acting) to solve these problems:

ReAct Architecture: The agent "thinks" about the user's request, selects the appropriate tool, and executes it.
Emergent Capabilities: leveraging Gemini 1.5 Flash to understand context and nuance.
Integrated Workflow: A unified chat interface for all security tools.
4. How to Load and Start
Prerequisites
Python 3.9+
Google Gemini API Key
Step 1: Start the Backend (The Brain)
Navigate to Assignment/backend or the root folder.
Run the automated setup script:
bash
fix_and_run.bat
Enter your Google API Key when prompted.
Wait for the message: [+] API Key and Model verified successfully!.
Step 2: Load the Extension (The Interface)
Open Chrome and go to chrome://extensions.
Enable Developer Mode (top right).
Click Load Unpacked.
Select the Assignment/extension folder.
Pin the "CyberGuardian" icon to your toolbar.
5. Test Cases
Once the system is running (Green Dot in extension), try these prompts:

Case A: Risk Calculation
Prompt: "Calculate risk for a server with 20 open ports and 5 critical vulns. Importance is 8."
Goal: Tests the agent's ability to parse natural language into mathematical logic.
Expected Output: "Risk Score: 140 (HIGH)".
Case B: Threat Intelligence
Prompt: "Check if malicious-domain.com is safe."
Goal: Tests external tool usage (simulated threat feed).
Expected Output: "Status: SUSPICIOUS/MALICIOUS".
Case C: Continuous Monitoring
Prompt: "Monitor logs for failed_login attempts. Threshold is 3."
Goal: Tests asynchronous autonomous behavior (the agent works in the background).
Expected Output: "Monitoring started..." followed by a result after 10 seconds.
6. Conclusion
CyberGuardian demonstrates how Agentic AI can transform security operations from reactive and manual to proactive and automated. By embedding intelligence directly into the analyst's workflow, we reduce burnout and improve response times.
