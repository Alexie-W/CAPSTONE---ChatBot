<template>
  <div class="signupverification container">
    <header>
      <img :src="getImageUrl('verificationbot.png')" alt="Avatar" class="avatar">
      <h1>Setting Up Your Profile</h1>
    </header>
      <!-- Loading section with a spinner and message -->
    <div class="loading-section">
      <div class="loader"></div>
      <p>{{ message }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Please wait while we set up your profile...' // Initial loading message
    };
  },
  mounted() {
    setTimeout(() => {
      this.message = 'Loading your dashboard...'; // Update message after profile setup
      setTimeout(() => {
        this.$router.push('/home');
      }, 3000); // Simulate loading time for dashboard
    }, 3000); // Simulate profile setup time
  },
  methods: {
    getImageUrl(image) {
      return new URL(`../assets/images/${image}`, import.meta.url).href;
    }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 100vh;
  background-color: #F5EFE6;
  padding: 20px;
}

header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 40px;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 20px;
}

h1 {
  color: #3C2317;
  font-size: 36px;
  margin: 0;
  font-family: "Copperplate", "Papyrus", fantasy;
}

.loading-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.loader {
  border: 16px solid #f3f3f3; /* Light grey */
  border-top: 16px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 120px;
  height: 120px;
  animation: spin 2s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

p {
  color: #3C2317;
  font-size: 18px;
}
</style>
