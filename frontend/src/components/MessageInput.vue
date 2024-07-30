<template>
  <input type="text" v-model="message" @keyup.enter="sendMessage" placeholder="Type a message..." class="message-input" />
</template>

<script>
export default {
  props: ['value'],
  data() {
    return {
      message: this.value || ''
    };
  },
  watch: {
    value(newValue) {
      this.message = newValue;
    }
  },
  methods: {
    sendMessage() {
      this.$emit('input', this.message);
      this.$emit('sendMessage');
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
