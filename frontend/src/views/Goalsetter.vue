<template>
   <!-- Main container for the goal setter page -->
  <div class="goals container">
    <header>
      <h1>Goals</h1>
    </header>
    <img :src="getImageUrl('goalbot.png')" alt="Avatar" class="avatar">
    <!-- Form to add a new goal -->
    <form @submit.prevent="addGoal" class="form-group">
      <input v-model="newGoal" placeholder="Set a new goal" required class="input">
      <button type="submit" class="btn add-btn">Add Goal</button>
    </form>
     <!-- List of goals -->
    <ul>
      <li v-for="goal in goals" :key="goal.GID" class="goal-item">
        <div class="goal-content">
          <input type="checkbox" v-model="goal.completed" class="checkbox">
          <span :class="{ completed: goal.completed }">{{ goal.g_description }}</span>
        </div>
        <!-- Progress tab shown when a goal is completed -->
        <div v-if="goal.completed" class="progress-tab">
          <div class="progress-bar">
            <div :style="{ width: getGoalProgress(goal) + '%' }" class="progress"></div>
          </div>
          <span>{{ getGoalProgress(goal) }}% Complete</span>
        </div>
        <button @click="removeGoal(goal.GID)" class="btn remove-btn">✕</button>
      </li>
    </ul>
  </div>
</template>

<script>
// Import axios for making HTTP requests
import axios from 'axios';

export default {
  data() {
    return {
      newGoal: '', // Model for new goal input
      goals: [], // List of goals
      nextGoalId: 1 // ID for the next goal to be added
    };
  },
   // Method to add a new goal
  methods: {
  async addGoal() {
    if (this.newGoal.trim() !== '') {
      const UID = localStorage.getItem('UID'); // Get the user ID from local storage
      const newGoal = {
        g_description: this.newGoal
      };
       // Send a POST request to add the new goal
      try {
        const response = await axios.post('/goal', {
          UID: UID,
          g_description: this.newGoal
        });
        // If the goal is added successfully, update the goals list
        if (response.data.message === 'Goal added successfully') {
          this.goals.push({
            ...newGoal,
            GID: this.nextGoalId,
            completed: false
          });
          this.nextGoalId += 1; // Increment the next goal ID
          this.newGoal = '';
        } else {
          alert('Failed to add goal. Please try again.');
        }
      } catch (error) {
        console.error('Error adding goal:', error);
        alert('An error occurred while adding the goal.');
      }
    } else {
      alert('Please enter a goal description.');
    }
  },// Method to remove a goal
  async removeGoal(GID) {
  try {
    const UID = localStorage.getItem('UID');
     // Send a DELETE request to remove the goal
    const response = await axios.delete(`/goal/${UID}/${GID}`);
    // If the goal is removed successfully, update the goals list
    if (response.data.message === 'Goal removed successfully') {
      this.goals = this.goals.filter(goal => goal.GID !== GID);
    } else {
      alert('Failed to remove goal. Please try again.');
    }
  } catch (error) {
    console.error('Error removing goal:', error);
    alert('An error occurred while removing the goal.');
  }
},
  removeGoal(GID) {
    this.goals = this.goals.filter(goal => goal.GID !== GID);
  },
  getImageUrl(image) {
    return new URL(`../assets/images/${image}`, import.meta.url).href;
  },
   // Method to calculate the progress of a goal
  getGoalProgress(goal) {
    //progress calculation (based on completion status)
    return goal.completed ? 100 : 0;
  }
}
};

</script>



<style scoped>
html, body {
  height: 100%;
  margin: 0;
}

.container {
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.goals {
  width: 100%;
  max-width: 600px;
  background-color: #F5EFE6;
  border-radius: 8px;
  padding: 20px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

header {
  text-align: center;
  margin-bottom: 20px;
}

h1 {
  color: #3C2317;
  font-size: 32px;
  margin: 0;
  font-family: "Copperplate", "Papyrus", fantasy;
}

.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  margin-top: 20px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.input {
  flex: 1;
  padding: 10px;
  margin-right: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.add-btn {
  background-color: #4CAF50;
  color: white;
}

.add-btn:hover {
  background-color: #45a049;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 100%;
}

.goal-item {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 10px;
  padding: 10px;
  background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: relative;
  width: 100%;
}

.goal-content {
  display: flex;
  align-items: center;
  width: 100%;
}

.checkbox {
  margin-right: 10px;
}

.completed {
  text-decoration: line-through;
  color: #888;
}

.remove-btn {
  position: absolute;
  bottom: 1px;
  right: 1px;
  background-color: rgba(220, 241, 245, 0.1); /* Very transparent background */
  color: rgba(0, 0, 0, 0.6); /* Slightly transparent color */
  border: none;
  border-radius: 50%;
  width: 10px; /* Tiny button size */
  height: 10px; /* Tiny button size */
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px; /* Tiny font size */
  cursor: pointer;
  font-weight: bold;
}

.remove-btn:hover {
  background-color: rgba(165, 234, 239, 0.3); /* Slightly more visible on hover */
}

.progress-tab {
  width: 100%;
  margin: 5px 0; /* Reduced margin */
  text-align: left;
}

.progress-bar {
  width: 100%;
  background-color: #ddd;
  border-radius: 4px;
  height: 10px; /* Small progress bar */
  margin: 5px 0;
  position: relative;
}

.progress {
  height: 100%;
  background-color: #4CAF50;
  border-radius: 4px;
  transition: width 0.3s ease;
}

span {
  display: block;
  margin-top: 5px;
  font-size: 12px; /* Smaller font size for progress */
}
</style>