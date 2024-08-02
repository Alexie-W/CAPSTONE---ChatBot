<template>
     <!-- Main container for the Meditation and Breathing Exercises page -->
  <div class="meditation container">
    <header>
      <h1>Guided Meditation and Breathing</h1>
      <img :src="getImageUrl('meditationbot.png')" alt="Avatar" class="avatar">
    </header>
     <!-- List of meditation options -->
    <div class="meditation-options">
      <div v-for="meditation in meditations" :key="meditation.id" class="meditation-option card">
        <input type="radio" v-model="selectedMeditation" :value="meditation" />
        <label>{{ meditation.name }}</label>
      </div>
    </div>
    <!-- Button to start the selected meditation session -->
    <button @click="startMeditation" class="btn">Start Meditation</button>
    <!-- Display meditation session content if available -->
    <div v-if="meditationContent" class="meditation-session card">
      <h2>Meditation Session</h2>
      <p>{{ meditationContent }}</p>
    </div>
    <!-- Display error message if there is an issue -->
    <div v-if="error" class="error card">
      <h2>Error</h2>
      <p>{{ error }}</p>
    </div>

    <!-- Embed YouTube Video -->
    <div v-if="youtubeEmbedUrl" class="youtube-video">
      <iframe width="560" height="315" :src="youtubeEmbedUrl" frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Meditation',
  data() {
    return {
       // Array of meditation options with video URLs
      meditations: [
        { id: 1, name: 'Stress Reduction', videoUrl: 'https://www.youtube.com/embed/wPoj5log_7M' },
        { id: 2, name: 'Self-Compassion', videoUrl: 'https://www.youtube.com/embed/tN1ZdVEanYY' },
        { id: 3, name: 'Focus', videoUrl: 'https://www.youtube.com/embed/wfDTp2GogaQ' },
        { id: 4, name: 'Sleep', videoUrl: 'https://www.youtube.com/embed/ccvL_gdXbKM' },
        
      ],
      selectedMeditation: null,  // Currently selected meditation option
      meditationContent: null, // Content for the selected meditation session
      error: null, // Error message for user feedback
      youtubeEmbedUrl: null // This will be updated based on the selected meditation
    };
  },
  methods: {
     // Method to start meditation based on selected option
    startMeditation() {
      if (!this.selectedMeditation) {
        this.error = 'Please select a meditation session.';
        return;
      }

      // Set the YouTube video URL for the selected meditation
      this.youtubeEmbedUrl = this.selectedMeditation.videoUrl;

     
      this.meditationContent = null; // Clear previous meditation content
      this.error = null;  // Clear any previous error
    },
    getImageUrl(image) {
      return new URL('../assets/images/${image}', import.meta.url).href;
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

.youtube-video {
  margin-top: 20px;
  text-align: center; /* Center the iframe */
}
</style>