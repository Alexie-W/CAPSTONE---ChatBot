<template>
  <div class="mood-tracker container">
     <!-- Title and prompt for the mood tracker -->
    <h2>Mood Tracker</h2>
    <p>How are you feeling today?</p>
     <!-- List of mood options -->
    <div class="mood-options flex">
      <div 
        v-for="mood in moods" 
        :key="mood.name" 
        class="mood-option card" 
        :class="{ selected: selectedMood === mood.name }"
        @click="selectMood(mood.name)"
      >
         <!-- Display mood image and name -->
        <img :src="getImageUrl(mood.image)" alt="" class="mood-image">
        <p>{{ mood.name }}</p>
      </div>
    </div>
    <!-- Text area for user to add notes about their mood -->
    <textarea v-model="moodNote" placeholder="Anything new happened today?" class="input-group"></textarea>
    <!-- Button to submit the mood and note -->
    <button @click="submitMood" class="btn">Submit</button>
      <!-- Display submitted entries -->
    <div class="entries">
      <div v-for="(entry, index) in entries" :key="index" class="entry card">
        <div class="entry-header">
          <img :src="getImageUrl(entry.mood.image)" alt="" class="entry-image">
          <p class="entry-mood">{{ entry.mood.name }}</p>
        </div>
        <!-- Display the note for each entry -->
        <p>{{ entry.note }}</p>
        <!-- Button to remove an entry -->
        <button @click="removeEntry(index)" class="remove-btn" title="Delete">✖</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // List of mood options with associated images
      moods: [
        { name: 'Happy', image: 'happy.png' },
        { name: 'Confused', image: 'confused.png' },
        { name: 'Angry', image: 'angry.png' },
        { name: 'Sad', image: 'sad.png' },
        { name: 'Scared', image: 'scared.png' },
      ],
      selectedMood: null, // Currently selected mood
      moodNote: '', // Note associated with the selected mood
      entries: [] // List of submitted mood entries
    };
  },
  methods: {
     // Method to get the URL for an image
    getImageUrl(image) {
      return new URL(`../assets/images/${image}`, import.meta.url).href;
    },
      // Method to select a mood
    selectMood(moodName) {
      this.selectedMood = moodName;
    },
     // Method to submit the selected mood and note
    submitMood() {
      if (this.selectedMood && this.moodNote.trim() !== '') {
         // Find the mood object based on the selected mood name
        const mood = this.moods.find(mood => mood.name === this.selectedMood);
          // Add the new entry to the list
        this.entries.push({ mood, note: this.moodNote });
          // Reset selected mood and note
        this.selectedMood = null;
        this.moodNote = '';
      }
    },
     // Method to remove an entry from the list
    removeEntry(index) {
      this.entries.splice(index, 1);
    }
  }
};
</script>

<style scoped>
.mood-tracker {
  text-align: center;
  margin: 20px;
  font-family: "Copperplate", "Papyrus", fantasy;
  background-color: #F5EFE6; /* Background color for the mood tracker page */
}

.mood-options {
  display: flex;
  justify-content: space-around;
  margin: 20px 0;
}

.mood-option {
  flex: 1;
  margin: 0 10px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.mood-option img {
  width: 80%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.mood-option.selected {
  border: 2px solid #4c86af;
  transform: scale(1.1);
}

textarea {
  width: 100%;
  height: 100px;
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #B4CDE6;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #628E90;
}
</style>
