<template>
  <div class="meditation container">
    <header>
      <h1>Guided Meditation and Breathing</h1>
      <img :src="getImageUrl('meditationbot.png')" alt="Avatar" class="avatar">
    </header>
    <div class="meditation-options">
      <div v-for="meditation in meditations" :key="meditation.id" class="meditation-option card">
        <input type="radio" v-model="selectedMeditation" :value="meditation" />
        <label>{{ meditation.name }}</label>
      </div>
    </div>
    <button @click="startMeditation" class="btn">Start Meditation</button>
    <div v-if="meditationContent" class="meditation-session card">
      <h2>Meditation Session</h2>
      <p>{{ meditationContent }}</p>
    </div>
    <div v-if="error" class="error card">
      <h2>Error</h2>
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Meditation',
  data() {
    return {
      meditations: [
        { id: 1, name: 'Stress Reduction' },
        { id: 2, name: 'Self-Compassion' },
        { id: 3, name: 'Focus' },
        // Add more meditation options as needed
      ],
      selectedMeditation: null,
      meditationContent: null,
      error: null
    };
  },
  methods: {
    async startMeditation() {
      if (!this.selectedMeditation) {
        this.error = 'Please select a meditation session.';
        return;
      }

      try {
        const response = await axios.post('https://the-guided-meditation-site.com', {
          meditationId: this.selectedMeditation.id
        });

        console.log('Response from external website:', response.data);
        this.meditationContent = response.data.content;  // Assuming response.data.content contains the meditation content
        this.error = null;  // Clear any previous error
      } catch (error) {
        console.error('Error starting meditation:', error);
        this.meditationContent = null;  // Clear any previous meditation content

        // Detailed error handling
        if (error.response) {
          console.error('Server responded with an error:', error.response.data);
          this.error = `Server error: ${error.response.data.message || error.response.statusText}`;
        } else if (error.request) {
          console.error('No response received:', error.request);
          this.error = 'No response received from the server. Please check your internet connection and try again.';
        } else {
          console.error('Error setting up the request:', error.message);
          this.error = `Error setting up the request: ${error.message}`;
        }
      }
    },
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
  border-radius: 8px;
}

header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 40px;
}

.avatar {
  width: 300px; 
  height: 300px; 
  border-radius: 0;
  margin-bottom: 20px;
}

h1 {
  color: #3C2317;
  font-size: 36px;
  margin: 0;
  font-family: "Copperplate", "Papyrus", fantasy;
}

.meditation-options {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin: 20px 0;
}

.meditation-option {
  flex: 1;
  margin: 10px;
  padding: 10px;
  text-align: center;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.btn {
  margin-top: 20px;
  padding: 20px 40px;
  background-color: #B4CDE6;
  color: black;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 18px;
}
.btn:hover {
  background-color: #628E90;
}

.meditation-session, .error {
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
