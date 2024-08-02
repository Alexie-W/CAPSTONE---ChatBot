<!-- src/components/TitlePage.vue -->
<template>
    <div class="title-page container">
      <header>
          <!-- Logo image for the page -->
        <img :src="getImageUrl('logo.png')" alt="Logo" class="logo">
          <!-- Avatar image for the page -->
        <img :src="getImageUrl('titlebot.png')" alt="Avatar" class="avatar">
          <!-- Main title of the page -->
        <h1>MENTAL MATE</h1>
      </header>
      <div class="buttons">
        <!-- Button to navigate to the sign-up page -->
        <button @click="navigateTo('signup')" class="btn">Sign Up</button>
          <!-- Button to navigate to the sign-in page -->
        <button @click="navigateTo('signin')" class="btn">Sign In</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
       // Method to navigate to a specified page using Vue Router
      navigateTo(page) {
        this.$router.push(`/${page}`);
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
    width: fit-content;
  }

  .logo {width: 50%;


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
  
  .buttons {
    display: flex;
    flex-direction: column;
    align-items: center;
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
  