# How CyberGuardian Works (Under the Hood)

You asked a great question: **"Does it analyze the website I'm visiting, or is it just calculating numbers I give it?"**

Here is the breakdown of the current system.

## 1. The Short Answer
Currently, **CyberGuardian is an "Input-Based Calculator"**, not an automatic scanner.

*   When you type: *"Calculate risk for 20 open ports..."* -> You are giving it the data manually.
*   It does **NOT** look at the website you have open in Chrome (yet).
*   It processes the numbers **you provide** and gives a score based on the logic we wrote in `backend/tools.py`.

## 2. The Data Flow (Step-by-Step)

When you press **Enter** in the extension popup:

1.  **Frontend (Chrome Extension)**:
    *   Takes your text (`"Calculate risk..."`).
    *   Sends it to your Python backend via HTTP POST (`http://127.0.0.1:8080/chat`).
    *   *Note: It does NOT send the URL of the current tab.*

2.  **Backend (Python Server)**:
    *   The **Agent (Gemini)** reads your text.
    *   It thinks: *"The user gave me numbers (20 ports, 5 vulns). I should use the `calculate_risk_score` tool."*
    *   It calls the Python function `calculate_risk_score(20, 5, 8)`.

3.  **The Tool (Logic)**:
    *   The function runs the math: `(20 * 0.5) + (5 * 5) * (8 / 2) = 140`.
    *   It returns: `140 (HIGH RISK)`.

4.  **The Response**:
    *   The Agent reads the result `140`.
    *   It generates a human-friendly answer: *"The risk score is 140, which is HIGH."*
    *   This text is sent back to the Chrome Extension to display.

## 3. How to Make it Scan Websites (Future Feature)

To make it automatically scan your current tab, we would need to:
1.  **Update `popup.js`**: Use `chrome.tabs.query` to get the current URL.
2.  **Send URL**: Pass `{ message: text, current_url: url }` to the backend.
3.  **New Tool**: Create a `scan_website(url)` tool in Python that uses a library like `requests` or `BeautifulSoup` to actually fetch the page content and look for vulnerabilities.

Right now, it is a **Assistant**, helping you calculate and reason about data you already have.
