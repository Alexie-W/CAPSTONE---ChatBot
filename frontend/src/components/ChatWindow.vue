<template>
  <div class="chat-window">
    <slot></slot>
  </div>
</template>

<style scoped>
.chat-window {
  display: flex;
  flex-direction: column;
  height: 100%;
}
</style>
