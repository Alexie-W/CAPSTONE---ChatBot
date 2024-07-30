<template>
  <div class="symptom-checker container">
    <h1>Are you feeling Unwell?</h1>
    <img :src="getImageUrl('drchopper.png')" alt="Unwell Image" class="unwell-image">
    <h2>Let's check your symptom</h2>
    <div class="symptoms">
      <div v-for="symptom in symptoms" :key="symptom.id" class="symptom card">
        <input type="checkbox" v-model="symptom.checked" />
        <label>{{ symptom.name }}</label>
      </div>
    </div>
    <button @click="addSymptomRequest" class="btn">Check Symptoms</button>
    <div v-if="results" class="results card">
      <h2>Results</h2>
      <p>{{ results }}</p>
    </div>
    <div v-if="error" class="error card">
      <h2>Error</h2>
      <p>{{ error }}</p>
    </div>
    <div v-if="entries.length" class="entries card">
      <h2>Previous Requests</h2>
      <ul>
        <li v-for="entry in entries" :key="entry.RID">
          {{ entry.symptom }} ({{ entry.request_date }})
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SymptomChecker',
  data() {
    return {
      symptoms: [
        { id: 1, name: 'Fever', checked: false },
        { id: 2, name: 'Cough', checked: false },
        { id: 3, name: 'Fatigue', checked: false },
        { id: 4, name: 'Headache', checked: false },
        { id: 5, name: 'Sore Throat', checked: false },
        { id: 6, name: 'Muscle Pains', checked: false },
      ],
      results: null,
      error: null,
      entries: [],
      UID: '12345' // Replace this with the actual user ID
    };
  },
  methods: {
    async addSymptomRequest() {
      const selectedSymptoms = this.symptoms.filter(symptom => symptom.checked).map(symptom => symptom.name);
      if (selectedSymptoms.length === 0) {
        this.error = 'Please select at least one symptom.';
        return;
      }

      try {
        const response = await axios.post('http://localhost:5000/request', {
          UID: this.UID,
          symptom: selectedSymptoms.join(', ')
        });

        this.results = response.data.message; // Assuming the response contains the message
        this.error = null; // Clear any previous error

        // Fetch updated list of entries
        this.fetchEntries();
      } catch (error) {
        console.error('Error adding request:', error);
        this.results = null; // Clear any previous results

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
    async fetchEntries() {
      try {
        const response = await axios.get(`http://localhost:5000/request/${this.UID}`);
        this.entries = response.data.requests;
      } catch (error) {
        console.error('Error fetching entries:', error);
        this.entries = [];
        if (error.response) {
          this.error = `Server error: ${error.response.data.message || error.response.statusText}`;
        } else if (error.request) {
          this.error = 'No response received from the server. Please check your internet connection and try again.';
        } else {
          this.error = `Error setting up the request: ${error.message}`;
        }
      }
    },
    getImageUrl(image) {
      return new URL(`../assets/images/${image}`, import.meta.url).href;
    }
  },
  mounted() {
    // Fetch the entries when the component is mounted
    this.fetchEntries();
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  text-align: center;
  background-color: #F5EFE6;
  font-family:"Copperplate", "Papyrus", fantasy;
}
.unwell-image {
  width: 100%;
  height: auto;
  max-width: 300px;
  margin: 20px auto;
  display: block;
}
.symptoms {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin: 20px 0;
  
}
.symptom {
  flex: 1 1 calc(33% - 20px);
  margin: 10px;
  padding: 10px;
  text-align: left;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.btn {
  padding: 10px 20px;
  background-color: #B4CDE6;
  color: black;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 20px;
  
}
.btn:hover {
  background-color: #628E90;
}
.results, .error {
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
