<template>
  <div class="create-profile container">
    <header>
      <img :src="getImageUrl('titlebot.png')" alt="Avatar" class="avatar">
      <h1>Create Profile</h1>
    </header>
    <form @submit.prevent="createProfile" class="form">
      <input v-model="firstName" placeholder="First Name" required class="input-group">
      <input v-model="lastName" placeholder="Last Name" required class="input-group">
      <input v-model="email" type="email" placeholder="Email" required class="input-group">
      <input v-model="password" type="password" placeholder="Password" required class="input-group">
      
      <vue-datepicker v-model="dob" :format="format" placeholder="Select Date of Birth" required class="input-group"></vue-datepicker>
      
      <div class="gender-selection">
        <label>
          <input type="radio" v-model="gender" value="Male" required>
          Male
        </label>
        <label>
          <input type="radio" v-model="gender" value="Female" required>
          Female
        </label>
      </div>
      
      <button type="submit" class="btn">Create Profile</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import DatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

export default {
  components: {
    'vue-datepicker': DatePicker
  },
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      dob: '',
      gender: '',
      format: 'yyyy-MM-dd' // Correct date format
    };
  },
  methods: {
    async createProfile() {
      const username = `${this.firstName} ${this.lastName}`;
      const UID = this.generateUID();
      
      const userData = {
        UID,
        username,
        email: this.email,
        password: this.password
      };
      
      try {
        const response = await axios.post('/api/register', userData);
        console.log(response.data.message);
        this.$router.push('/SignupVerification');
      } catch (error) {
        console.error('Error creating profile:', error);
      }
    },
    generateUID() {
      return '_' + Math.random().toString(36).substr(2, 9);
    },
    getImageUrl(image) {
      if (!image) {
        console.error('Image name is undefined');
        return ''; // Return an empty string or placeholder image
      }
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

.form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input-group {
  width: 80%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 18px;
}

.gender-selection {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.gender-selection label {
  margin: 0 20px;
  font-size: 18px;
  color: #3C2317;
}

.gender-selection input[type="radio"] {
  margin-right: 10px;
}

.btn {
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
</style>
