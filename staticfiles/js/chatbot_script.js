document.getElementById('chat-icon').addEventListener('click', () => {
    const chatbotContainer = document.getElementById('chatbot-container');
    chatbotContainer.style.display = chatbotContainer.style.display === 'none' ? 'block' : 'none';
});

document.getElementById('chatbot-send-button').addEventListener('click', sendMessage);
document.getElementById('chatbot-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});


async function sendMessage() {
    const userMessage = document.getElementById('chatbot-input').value.trim();
    if (!userMessage) return;

    // Display user message
    const chatContent = document.getElementById('chatbot-content');
    chatContent.innerHTML += `<div class="chatbot-message user">${userMessage}</div>`;
    document.getElementById('chatbot-input').value = '';

    // Fetch chatbot response from backend API
    try {
        const response = await fetch("{% url 'chatbot' %}", {
            method: "POST",
            body: JSON.stringify({ query: userMessage }),
            headers: {
                'Content-Type': 'application/json',
            },
        });
        const data = await response.json();
        if (data.response) {
            chatContent.innerHTML += `<div class="chatbot-message bot">${data.response}</div>`;
        } else {
            chatContent.innerHTML += `<div class="chatbot-message bot">Sorry, something went wrong.</div>`;
        }
    } catch (error) {
        chatContent.innerHTML += `<div class="chatbot-message bot">Error: ${error.message}</div>`;
    }
}
