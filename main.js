
url=''
document.addEventListener('DOMContentLoaded', function () {
const fileUrl = 'token.txt'; // Replace with the actual URL
fetch(fileUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.text();
    })
    .then(content => {
        console.log(content);
        url = content;
        
    })
    .catch(error => {
        console.error('Error fetching the file:', error);
    });

    const d = new Date();
    var t = document.getElementById('timee');
    const now = new Date();
    t.innerHTML = now.toLocaleTimeString([], {hour: '2-digit', minute: '2-digit' });

  const messageInput = document.querySelector('.form-control');
  const sendButton = document.querySelector('.send-icon');
  const chatContainer = document.querySelector('.msg-page');

  // Add an event listener to handle sending messages when the send button is clicked
  sendButton.addEventListener('click', function () {
    sendMessage();
  });

  // Alternatively, you can handle sending messages when the Enter key is pressed
  messageInput.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
      sendMessage();

}
    



  function sendMessage() {
    const userMessage = messageInput.value;
    if (userMessage.trim() !== '') {
      displayOutgoingMessage(userMessage);
      messageInput.value = '';
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }
  }


  function displayOutgoingMessage(message) {
    const outgoingChat = document.createElement('div');
    outgoingChat.classList.add('outgoing-chats');
    outgoingChat.innerHTML = `
      <div class="outgoing-chats-img">
        <img src="images.jpg" />
      </div>
      <div class="outgoing-msg">
        <div class="outgoing-chats-msg">
          <p class="multi-msg">
            ${message}
          </p>
          <span class="time">${getCurrentTime()}</span>
        </div>
      </div>
    `;
    chatContainer.appendChild(outgoingChat);
    fetch( url+'/gen_response?q='+ message, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
          },
        body: JSON.stringify({ data: "inputData" }),
})
.then(response => response.json())
.then(data => {
displayIncomingMessage(data['message'])
  console.log(data['message']);
})
.catch(error => console.error('Error:', error));
  }

  function displayIncomingMessage(message) {
    const incomingChat = document.createElement('div');
    incomingChat.classList.add('received-chats');
    incomingChat.innerHTML = `
          <div class="received-chats">
            <div class="received-chats-img">
              <img src="OIP.gif" />
            </div>
            <div class="received-msg">
              <div class="received-msg-inbox">
                <p class="single-msg">
                  ${message}
                </p>
                <span class="time">${getCurrentTime()}</span>
              </div>
            </div>
          </div>`;

    chatContainer.appendChild(incomingChat);
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }

  function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString([], {hour: '2-digit', minute: '2-digit' });
  }
});

})
