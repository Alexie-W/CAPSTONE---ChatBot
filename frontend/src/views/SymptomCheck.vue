<template>
  <div class="symptom-checker container">
      <!-- Main Title Question of the page -->
    <h1>Are you feeling Unwell?</h1>
    <img :src="getImageUrl('drchopper.png')" alt="Unwell Image" class="unwell-image">
     <!-- Subtitle prompting user to check symptoms -->
    <h2>Let's check your symptoms</h2>

    <div class="symptoms">
      <!-- Button to redirect to external symptom checker -->
      <button @click="redirectToSymptomChecker" class="btn">Use External Symptom Checker</button>

      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
   // Method to redirect the user to an external symptom checker site
  name: 'SymptomChecker',
  methods: {
    redirectToSymptomChecker() {
      window.location.href = 'https://symptomate.com/interview/0'; // Redirect to external site
    },
    getImageUrl(image) {
      return new URL("../assets/images/${image}", import.meta.url).href;
    }
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