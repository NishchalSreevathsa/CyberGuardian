document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const chatWindow = document.getElementById('chat-window');
    const statusIndicator = document.getElementById('status');

    // Check Status periodically
    checkBackendStatus();
    setInterval(checkBackendStatus, 10000);

    // Event Listeners
    sendBtn.addEventListener('click', sendMessage);
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    async function checkBackendStatus() {
        try {
            // Using a simple fetch with short timeout
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), 2000);

            await fetch('http://127.0.0.1:8080/docs', {
                method: 'HEAD',
                signal: controller.signal
            });
            clearTimeout(timeoutId);

            statusIndicator.classList.add('online');
            statusIndicator.title = "Backend Online";
        } catch (e) {
            statusIndicator.classList.remove('online');
            statusIndicator.title = "Backend Offline";
        }
    }

    async function sendMessage() {
        const text = input.value.trim();
        if (!text) return;

        addMessage("user", text);
        input.value = '';
        input.disabled = true;

        // Show a loading indicator in chat
        const loadingId = "loading-" + Date.now();
        addLogEntry("Thinking...", loadingId);

        try {
            const response = await fetch('http://127.0.0.1:8080/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });

            // Remove loading indicator equivalent logic (here we just append)
            // Ideally we'd remove the "Thinking..." or replace it.
            // For now, we just append logs after.

            if (!response.ok) throw new Error('Network response was not ok');

            const data = await response.json();

            // Display Logs (Thoughts)
            if (data.logs && data.logs.length > 0) {
                data.logs.forEach(log => {
                    addLogEntry(log);
                });
            }

            // Display Final Answer
            addMessage("agent", data.response);

        } catch (error) {
            addMessage("system", "Error communicating with agent: " + error.message);
        } finally {
            input.disabled = false;
            input.focus();
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }
    }

    function addMessage(role, text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${role}`;

        const bubble = document.createElement('div');
        bubble.className = 'bubble';
        bubble.innerHTML = text.replace(/\n/g, '<br>');

        msgDiv.appendChild(bubble);
        chatWindow.appendChild(msgDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function addLogEntry(text, id = null) {
        const logDiv = document.createElement('div');
        logDiv.className = 'log-entry';
        logDiv.textContent = "> " + text;
        if (id) logDiv.id = id;
        chatWindow.appendChild(logDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});
