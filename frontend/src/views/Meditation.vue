<template>
    <div class="meditation container">
      <h1>Guided Meditation</h1>
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
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    padding: 20px;
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
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .btn:hover {
    background-color: #45a049;
  }
  .meditation-session, .error {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  </style>
  