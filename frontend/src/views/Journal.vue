<template>
  <div class="journal container">
    <header>
      <h1>Journal</h1>

      <img :src="getImageUrl('journalbot.png')" alt="Avatar" class="avatar">
    </header>
    <button @click="toggleEntryBox" v-if="!showEntryBox" class="btn">Add New Entry</button>
    <div v-if="showEntryBox" class="entry-box">
      <textarea v-model="entry" placeholder="Write your thoughts here..." class="input-group"></textarea>
      <button @click="saveEntry" class="btn">Save Entry</button>
    </div>
    <div class="entries">
      <div v-for="(entry, index) in entries" :key="index" class="entry card">
        <p>{{ entry }}</p>
        <button @click="removeEntry(index)" class="remove-btn" title="Delete">✖</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      entry: '',
      entries: [],
      showEntryBox: false
    };
  },
  methods: {
    toggleEntryBox() {
      this.showEntryBox = !this.showEntryBox;
    },
    saveEntry() {
      if (this.entry.trim() !== '') {
        this.entries.push(this.entry);
        this.entry = '';
        this.showEntryBox = false;
      }
    },
    removeEntry(index) {
      this.entries.splice(index, 1);
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

.btn {
  margin-top: 20px;
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

.input-group {
  width: 100%;
  height: 200px;
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 18px;
}

.entries {
  margin-top: 40px;
  width: 100%;
}

.entry {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
  background-color: #B4CDE6;
  font-size: 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.remove-btn {
  background-color: #FF6347;
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
  position: relative;
}

.remove-btn::after {
  content: 'Delete';
  position: absolute;
  bottom: 120%;
  left: 50%;
  transform: translateX(-50%);
  background-color: #333;
  color: white;
  padding: 5px;
  border-radius: 4px;
  opacity: 0;
  white-space: nowrap;
  pointer-events: none;
  transition: opacity 0.2s;
}

.remove-btn:hover::after {
  opacity: 1;
}

.entry-box {
  margin-bottom: 40px;
  width: 100%;
}
</style>
