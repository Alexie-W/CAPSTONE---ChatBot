<template>
  <button @click="$emit('sendMessage')" class="send-btn">Send</button>
</template>

<style scoped>
.send-btn {
  padding: 10px 20px;
  background-color: #628E90;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
}
.send-btn:hover {
  background-color: #4CAF50;
}
</style>
