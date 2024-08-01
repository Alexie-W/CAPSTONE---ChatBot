<template>
  <div class="chat container">
    <header class="chat-header">
      <!-- <img :src="getImageUrl('matebot.png')" alt="Avatar" class="avatar"> -->
      <h1>Chat with Mate</h1>
    </header>
    <ChatWindow>
      <div class="message-list-container">
        <MessageList :messages="messages" />
      </div>
      <div class="message-input-container">
        <MessageInput v-model="newMessage" @sendMessage="sendMessage" />
        <SendMessageButton @sendMessage="sendMessage" />
      </div>
    </ChatWindow>
  </div>
</template>
<script>
import axios from 'axios';
import ChatWindow from '../components/ChatWindow.vue';
import MessageInput from '../components/MessageInput.vue';
import MessageList from '../components/MessageList.vue';
import SendMessageButton from '../components/SendMessageButton.vue';

export default {
  components: {
    ChatWindow,
    MessageInput,
    MessageList,
    SendMessageButton
  },
  data() {
    return {
      messages: [],
      newMessage: '',
      userId: null
    };
  },
  methods: {
    async sendMessage() {
  if (this.newMessage.trim() !== '') {
    const user_id = localStorage.getItem('UID');
    // Add the user's message to the message list
    this.messages.push({ text: this.newMessage, sender: 'user' });

    // Send the message to the backend
    try {
      const response = await axios.post('http://localhost:5000/chatbot', {
        message: this.newMessage,
        user_id: user_id
      });
      this.messages.push({ text: response.data.response, sender: 'bot' });
    } catch (error) {
      console.error("Error sending message to backend:", error);
      this.messages.push({ text: "There was an error processing your message.", sender: 'bot' });
    }

    this.newMessage = '';
  }
}
    },
    getImageUrl(image) {
      return new URL('../assets/images/${image}', import.meta.url).href;
    }
  };

</script>

<style scoped>
.chat {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #F5EFE6; /* Background color for the chat page */
}

.chat-header {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  background-color: #B4CDE6;
  border-bottom: 1px solid #ddd;
}

.avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 20px;
}

h1 {
  color: #3C2317; /* Text color for the header */
  font-size: 24px;
  margin: 0;
  font-family: "Copperplate", "Papyrus", fantasy;
}

.message-list-container {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  background-color: #ffffff;
}

.message-input-container {
  display: flex;
  padding: 10px;
  background-color: #B4CDE6;
  border-top: 1px solid #ddd;
}

.message-input-container input {
  flex: 1;
  margin-right: 10px;
}

.btn {
  padding: 10px 20px;
  background-color: #628E90;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
}
.btn:hover {
  background-color: #4CAF50;
}
</style>
