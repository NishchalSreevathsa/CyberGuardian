# CyberGuardian User Guide

This guide walks you through running the Session 3 Assignment, loading the extension, and verifying the UI features.

---

## Part 1: Start the "Brain" (Backend)

The "Brain" is a Python server that does the intelligent processing (Risk calculation, Threat checking, etc.).

1.  **Open the Folder**: Go to `d:\Nishchal\School of AI\Session 3`.
2.  **Run the Script**: Double-click `run_assignment.bat`.
3.  **Check the Output**:
    *   A black terminal window should open.
    *   It will check for Python and install `fastapi`, `uvicorn`, etc.
    *   **Success Message**: Look for `Uvicorn running on http://127.0.0.1:8080`.
    *   **Keep this window OPEN**. If you close it, the extension will stop working.

> **Important**: You need a Google API Key.
> *   If the script crashes or says "API Key not found", open `Assignment\backend\server.py` in a text editor (Notepad or VS Code).
> *   Find line 15: `GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")`
> *   Change it to: `GOOGLE_API_KEY = "your_actual_api_key_here"` (put your key inside quotes).
> *   Save and run the `.bat` file again.

---

## Part 2: Load the "Face" (Chrome Extension)

1.  **Open Chrome**.
2.  In the address bar, type: `chrome://extensions` and hit Enter.
3.  **Enable Developer Mode**: Look at the top-right corner. Toggle the switch to **ON**.
4.  **Load the Extension**:
    *   Click the **Load unpacked** button (top-left).
    *   Navigate to: `d:\Nishchal\School of AI\Session 3\Assignment\extension`.
    *   **Select the Folder** (`extension`) and click Select/OK.
5.  **Pin It**:
    *   Click the Puzzle Piece icon 🧩 in your Chrome toolbar.
    *   Find "CyberGuardian AI Agent" and click the Pin 📌 icon.
    *   You should now see a green/black icon in your toolbar.

---

## Part 3: Verify & Test Features

Click the CyberGuardian icon to open the popup.

### 1. Check Technical Connection
*   **Look at the Status Dot**: In the top-right of the popup header, there is a small dot.
    *   🟢 **Green**: Backend is connected. Good to go!
    *   🔴 **Red**: Backend is offline. Check if your black terminal window is still running.

### 2. Check UI Elements
*   **Design**: Verify it has a dark theme (Cyberpunk style) with green accents.
*   **Chat Window**: You should see a welcome message: "Welcome, Analyst..."
*   **Input Box**: A text box at the bottom to type commands.

### 3. Feature Tests (The Assignment)

**Test A: Risk Calculation (Logic Test)**
*   *Type*: "Calculate risk for a server with 20 open ports and 5 critical vulns. Importance is 8."
*   *Expected Result*:
    *   The Agent will "Think" (show logs).
    *   It should tell you the **Risk Score** (high number) and categorize it (e.g., CRITICAL).

**Test B: Threat Intelligence (External Tool Test)**
*   *Type*: "Check if phishing.com is safe."
*   *Expected Result*:
    *   It should reply that the domain is **MALICIOUS** (this is hardcoded in `tools.py` for the demo).

**Test C: Continuous Monitoring (Loop Test)**
*   *Type*: "Monitor logs for failed_login for 5 seconds."
*   *Expected Result*:
    *   The backend terminal will show "Monitoring...".
    *   The Extension will wait (showing "Thinking...").
    *   After 5 seconds, it will report back whether it found any events.

---

## Troubleshooting
*   **"NetworkError when attempting to fetch resource"**: Your backend server is not running. Double-click `run_assignment.bat` again.
*   **"Error: GOOGLE_API_KEY not found"**: You didn't set the API key in Step 1.
