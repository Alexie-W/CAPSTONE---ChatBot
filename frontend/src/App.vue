<!-- App.vue -->
<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
/* Add global styles here */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
}

#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f5f5f5;
}

h1, h2, h3, h4, h5, h6 {
  color: #333;
  margin: 0 0 20px;
  font-weight: 400;
}

p {
  color: #666;
  line-height: 1.6;
  margin: 0 0 20px;
}

button {
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.card {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 20px 0;
}

.flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.flex-column {
  display: flex;
  flex-direction: column;
}

.input-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.input-group label {
  margin-bottom: 5px;
  font-weight: 500;
}

.input-group input,
.input-group textarea {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
}

.input-group textarea {
  resize: vertical;
}

.navbar {
  background-color: #007BFF;
  padding: 15px;
  color: #fff;
  width: 100%;
  text-align: center;
}

.navbar a {
  color: #fff;
  text-decoration: none;
  margin: 0 15px;
}

.navbar a:hover {
  text-decoration: underline;
}

.footer {
  background-color: #007BFF;
  color: #fff;
  padding: 15px;
  text-align: center;
  width: 100%;
  position: fixed;
  bottom: 0;
}

</style>
