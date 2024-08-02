<template> 
 <!-- Input field for typing messages -->
  <input type="text" v-model="message" @keyup.enter="sendMessage" placeholder="Type a message..." class="message-input" />
</template>

<script>
export default {
   // Declare 'value' as a prop for the component
  props: ['value'],
  data() {
    return {
      // Initialize message data with the prop value if provided
      message: this.value || ''
    };
  },
  watch: {
      // Watch for changes in the 'value' prop and update the message data
    value(newValue) {
      this.message = newValue;
    }
  },
  methods: {
      // Method to handle sending the message
    sendMessage() {
      this.$emit('input', this.message);   // Emit 'input' event with the current message
      this.$emit('sendMessage'); // Emit 'sendMessage' event to notify that a message is being sent
      this.message = ''; // Clear the message after sending
    }
  }
};
</script>

<style scoped>
.message-input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
}
</style>
