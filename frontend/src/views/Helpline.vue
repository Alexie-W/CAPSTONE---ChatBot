<template>
    <div class="help-services container">
      <header>
        <h1>Help and Support Services</h1>

        <img :src="getImageUrl('helpbot.png')" alt="Help Avatar" class="avatar">
        
      </header>
      <div class="services-list">
        <div v-for="service in services" :key="service.id" class="service card">
          <h2>{{ service.name }}</h2>
          <p>{{ service.description }}</p>
          <p><strong>Contact:</strong> {{ service.contact }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        services: [
          { id: 1, name: 'Mental Health and Suicide Prevention Helpline', description: '24/7, free and confidential support for people in distress.', contact: '888-639-5433' },
          { id: 2, name: 'SafeSpot', description: 'SafeSpot is Jamaica’s national child and teen helpline.', contact: '888-723-3776' },
        ]
      };
    },
    methods: {
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
    font-size: 24px;
    margin: 0;
    font-family: "Copperplate", "Papyrus", fantasy;
  }
  
  .services-list {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .service {
    width: 80%;
    padding: 20px;
    margin: 10px 0;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    color: #3C2317;
    font-size: 20px;
    margin: 0 0 10px;
  }
  
  p {
    color: #3C2317;
    font-size: 16px;
    margin: 5px 0;
  }
  </style>
  