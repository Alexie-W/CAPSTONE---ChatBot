<template>
  <div class="sign-in container">
    <header>
      <img :src="getImageUrl('logo.png')" alt="Logo" class="logo">
      <h1>MENTAL MATE</h1>
      <img :src="getImageUrl('titlebot.png')" alt="Avatar" class="avatar">
    </header>
    <!-- Welcome message and instructions -->
    <h2>Welcome Back</h2>
    <h4>Enter your password and email to sign in</h4>
       <!-- Sign-in form -->
    <form @submit.prevent="signIn" class="form">
      <input v-model="email" type="email" placeholder="Email" required class="input-group">
      <input v-model="password" type="password" placeholder="Password" required class="input-group">
      <br>
       <!-- Link to sign-up page for users without an account -->
      <h5 class="sign-up-link">
        Don't have an account?
        <router-link to="/signup" class="link">Sign Up</router-link>
      </h5>
      <!-- Submit button for the sign-in form -->
      <button type="submit" class="btn">Sign In</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '', // User's email input
      password: '' // User's password input
    };
  },
  methods: {
    // Method to handle sign-in process
    async signIn() {
      try {
        // Send a POST request to the login endpoint with email and password
        const response = await axios.post('/api/login', {
          email: this.email,
          password: this.password
        });
          // Check if login was successful and UID was returned
        if (response.data.UID) {
          console.log('Login successful:', response.data);
          localStorage.setItem('UID', response.data.UID);
          this.$router.push('/home');
        } else {
            // Log error if credentials are invalid
          console.error('Invalid credentials'); 
        }
      } catch (error) {
        console.error('Error during sign in:', error);   // Log any errors that occur during sign-in
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
  margin-bottom: 30px; /* Adjust based on wireframes */
}

.logo {
  width: 100px; /* Adjust size according to wireframes */
  height: auto;
}

.avatar {
  width: 150px; /* Adjust size according to wireframes */
  height: 150px; /* Adjust size according to wireframes */
  border-radius: 50%; /* Apply rounded corners if specified in wireframes */
  margin-bottom: 20px;
}

.sign-in {
  text-align: center;
  font-weight: bold;
}

h1 {
  font-size: 2em; /* Adjust as needed */
  margin: 10px 0;
}

h2 {
  color: #3C2317;
  font-size: 26px;
  margin: 0;
  font-family: "Copperplate", "Papyrus", fantasy;
}
.form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sign-up-link {
  margin-top: 20px;
}

.link {
  color: #B4CDE6; 
  text-decoration: none;
  font-weight: bold;
}

.link:hover {
  text-decoration: underline;
}

.input-group {
  width: 150%; /* Adjust width if needed */
  padding: 12px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 50px;
  box-sizing: border-box; /* Ensures padding and border are included in the width */
}

.btn {
  padding: 15px 30px;
  background-color: #B4CDE6;
  color: black;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 18px;
  margin: 10px 0;
}
.btn:hover {
  background-color: #628E90;
}
</style>
