<template>
  <div class="home">
    <header>
      <h1> DASHBOARD </h1>
    </header>
    <router-link v-for="option in options" :key="option.title" :to="option.route" class="card">
      <img :src="getImageUrl(option.image)" alt="">
      <h3>{{ option.title }}</h3>
      <p>{{ option.description }}</p>
    </router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      options: [
        { title: "Let's chat", description: "Talk with Mate", image: 'chatdash.png', route: '/chat' },
        { title: "Breathing and Meditation", description: "Breathe, Flow, Transform", image: 'meditatedash.png', route: '/meditation' },
        { title: "Mood Tracker", description: "How are you feeling?", image: 'mooddash.png', route: '/moodtracker' },
        { title: "Symptom Checker", description: "Check your illness", image: 'symptomdash.png', route: '/symptomcheck' },
        { title: "Journal Entry", description: "Write down your feelings", image: 'journaldash.png', route: '/journal' },
        { title: "Goal Setting", description: "What do you want to accomplish?", image: 'goaldash.png', route: '/goalsetter' },
        { title: "Interractive Quizzes", description: "Can you answer all the questions?", image: 'quizdash.png', route: '/quiz' },
        { title: "Helpline Services", description: "Feel Free to reach out", image: 'helpdash.png', route: '/helpline' },
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

<style>
.home {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
  background-color: #F5EFE6; /* Background color for the home page */
  padding: 20px;
  min-height: 100vh;
}

header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  width: 100%;
  background-color: #F5EFE6; /* Header background color */
  padding: 10px;
  border-radius: 8px;
}

h1 {
  color: 3C2317; /* Text color for the header */
  font-size: 24px;
  margin: 0;
  font-family:"Copperplate", "Papyrus", fantasy;
}

.options {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 100%;
}

.card {
  width: 30%;
  margin: 1%;
  text-align: center;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-decoration: none;
  color: inherit;
  background-color: #B4CDE6; 
  transition: transform 0.2s, box-shadow 0.2s;

}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.card img {
  width: 100px; 
  height: 100px; /* Adjust the height of the images */
  object-fit: cover; /* Ensure the images cover the area without stretching */
  border-radius: 8px;
}


h3 {
  margin: 10px 0 5px;
  color: #333;
}

p {
  color: #666;
}
</style>
