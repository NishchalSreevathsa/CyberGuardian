# CyberGuardian Agent: Video Presentation Script

**Project Title:** CyberGuardian - A Smart Agentic Analysis Tool for SOC Analysts

---

## 1. Introduction (1 min)

*   **Intro:** "Hello, I am [Your Name]. Today I am presenting my project for School of AI Session 3: **CyberGuardian**."
*   **What is it?**: A Chrome Extension powered by an **AI Agent (Gemini 1.5 Flash)** that helps cybersecurity professionals analyze threats, calculate risks, and monitor logs instantly without leaving their browser.
*   **Goal**: To reduce the mental load on analysts by automating routine calculations and threat checks using Agentic AI.

---

## 2. The Problem: Current Industry Challenges (2 mins)

Why did I build this? In the cybersecurity industry today:
1.  **Tool Fatigue**: Analysts have to switch between 10+ tabs (SIEM, Threat Intel, Calculator, Spreadsheets) just to triage one alert.
2.  **Alert Overload**: Tier 1 analysts are drowning in logs. They need a "second brain" to quickly filter noise from real threats.
3.  **Manual Calculations**: Assessing risk often involves manual math (CVSS scores + Asset Value). It's slow and prone to human error.
4.  **Static Workflows**: Traditional scripts are rigid. If the situation changes, the script breaks. We need flexible, intelligent agents.

---

## 3. The Solution: CyberGuardian (Agentic AI) (2 mins)

My solution is not just a chatbot—it is a **Self-Correction & Reasoning Agent** built on the principles of **Agentic AI**.

**Key Architectural Concepts Used:**
1.  **ReAct Loop (Reasoning + Acting)**: The agent doesn't just guess. It follows a "Thought -> Action -> Observation" cycle. It *thinks* about the problem, *selects* a tool, *observes* the output, and then *answers*.
2.  **Emergent Capabilities**: Using **Gemini 1.5 Flash**, the model displays emergent behaviors—like understanding context and making decisions—that were not explicitly hardcoded.
3.  **Strict System Prompting**: I engineered the system prompt to avoid hallucinations and force the model to be **Goal-Directed** (one of the core pillars of agency).

**How it differs from a standard LLM:**
*   **Standard LLM**: Passive. "Here is a poem about cybersecurity."
*   **CyberGuardian Agent**: Active. "I will calculate the risk score using the Python tool I have access to."

---

## 4. Live Demo (5-8 mins)

*(Action: Screen share your desktop folder)*

### Step 1: Running the Agent (Backend)
"First, let's start the Brain of the agent."
1.  Open the `Session 3` folder.
2.  Run **`fix_and_run.bat`**.
3.  *(Show the terminal)*: "It automatically updates libraries, checks my API Key, and selects the best model (**Gemini 1.5 Flash**). Once we see 'Verified', we are ready."

### Step 2: The Extension (Frontend)
"Now, let's open Chrome."
1.  Click the **CyberGuardian Icon**.
2.  *(Show the UI)*: "We have a cyberpunk-themed interface. The Green Dot means the backend is connected via **Async/Await** (non-blocking) communication."

---

### Step 3: Test Cases (Evaluating Agent Behavior)

#### Case A: Risk Calculation (Logic & Reasoning)
*   **Concept**: Testing the **ReAct Loop**.
*   **Prompt**: *"Calculate risk for a server with 20 open ports and 5 critical vulns. Importance is 8."*
*   **Analysis**:
    *   *(Point to the terminal logs)*: "Look at the logs. You see 'Thinking...' then 'Calling Tool'. This is the **Chain of Thought**. The agent *chose* the `calculate_risk_score` function because it understood the intent."
*   **Output**: "Risk Score: 140 (HIGH)".

#### Case B: Threat Intelligence (External Tool Use)
*   **Concept**: Moving beyond the LLM's internal knowledge (**RAG-like behavior**).
*   **Prompt**: *"Check if malicious-domain.com is safe."*
*   **Analysis**: "An LLM alone would hallucinate an answer. But my Agent knows it doesn't know. It calls the `check_threat_intel` tool to get ground truth."
*   **Output**: "Status: SUSPICIOUS/MALICIOUS".

#### Case C: Continuous Monitoring (Async Autonomy)
*   **Concept**: **Autonomous Action & Persistence**.
*   **Prompt**: *"Monitor logs for failed_login attempts. Threshold is 3."*
*   **Analysis**: "Here we see **Asynchronous execution**. The frontend waits while the backend runs a monitoring loop. The agent is maintaining **state** and waiting for a trigger."
*   **Output**: "Threshold breached/not breached."

---

## 5. Conclusion (1 min)

*   **Summary**: CyberGuardian proves that Agentic AI is not just for chatbots—it can be a powerful tool for Security Operations.
*   **Future**: I plan to add real API connections (VirusTotal, Splunk) to make this a production-ready tool.
*   "Thank you for watching."
