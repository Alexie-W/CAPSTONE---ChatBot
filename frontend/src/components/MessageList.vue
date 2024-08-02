<template>
    <!-- Container for displaying the list of messages -->
  <div class="message-list">
      <!-- Iterate over messages and display each one -->
    <div v-for="(message, index) in messages" :key="index" class="message" :class="{'user-message': message.sender === 'user', 'bot-message': message.sender === 'bot'}">
       <!-- Display the text of each message -->
      <p>{{ message.text }}</p>
    </div>
  </div>
</template>

<script>
  // Declare 'messages' as a prop for the component
export default {
  props: ['messages']
};
</script>

<style scoped>
.message-list {
  display: flex;
  flex-direction: column;
}

.message {
  margin: 5px 0;
  padding: 10px;
  border-radius: 8px;
  max-width: 60%;
}

.user-message {
  align-self: flex-end;
  background-color: #B4CDE6;
}

.bot-message {
  align-self: flex-start;
  background-color: #F5EFE6;
}
</style>
