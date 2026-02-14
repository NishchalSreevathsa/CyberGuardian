# CyberGuardian Agent - Setup Instructions

## 1. Prerequisites
*   Python 3.9+ installed.
*   Google Gemini API Key (Get one from [Google AI Studio](https://aistudio.google.com/)).

## 2. Backend Setup
1.  Open a terminal in `School of AI/Session 3/Assignment/backend`.
2.  Install dependencies:
    ```powershell
    pip install -r requirements.txt
    ```
3.  Set your API Key:
    ```powershell
    $env:GOOGLE_API_KEY="your_api_key_here"
    ```
    *(Or just paste it directly into server.py if strictly testing locally)*
4.  Run the server:
    ```powershell
    python server.py
    ```
    You should see: `Uvicorn running on http://127.0.0.1:8080`

## 3. Extension Setup
1.  Open Google Chrome.
2.  Go to `chrome://extensions`.
3.  Enable **Developer Mode** (top right toggle).
4.  Click **Load Unpacked**.
5.  Select the `School of AI/Session 3/Assignment/extension` folder.
6.  Pin the "CyberGuardian" extension to your toolbar.

## 4. Testing the Agent
Click the extension icon. If the status dot is Green, you are connected.

**Try these commands:**
*   **Risk Calc**: *"Calculate the risk score for a server with 10 open ports and 5 critical vulnerabilities. It is a high value asset (score 9)."*
*   **Threat Check**: *"Is malicious-domain.com safe?"*
*   **Monitoring**: *"Monitor the logs for failed_login attempts. Alert me if there are more than 3."* (This will run for 10 seconds in the backend).

## 5. Troubleshooting
*   **Red Status Dot**: Ensure `server.py` is running and port 8080 is not blocked.
*   **"Error communicating"**: Check the terminal running `server.py` for Python errors.
*   **Agent loops/fails**: Ensure your API Key is valid.
