<template>
    <div class="quiz container">
      <header>

        <h1>Quiz</h1>

        <img :src="getImageUrl('quizbot.png')" alt="Avatar" class="avatar">  
      </header>
      
      <div v-if="quizzes.length" class="quizzes-list">
        <div v-for="quiz in quizzes" :key="quiz.QID" class="quiz-item card">
          <h2>Quiz ID: {{ quiz.QID }}</h2>
          <p>Date: {{ formatDate(quiz.quiz_date) }}</p>
          <button @click="viewQuiz(quiz.QID)" class="btn">View Quiz</button>
        </div>
      </div>
      
      <div v-else class="no-quizzes card">
        <h2>No Quizzes Found</h2>
        <p>You have no quizzes available.</p>
      </div>
      
      <div v-if="selectedQuiz" class="quiz-details card">
        <h2>Quiz Details</h2>
        <div v-for="question in selectedQuiz.questions" :key="question.question_id" class="question-item">
          <p>{{ question.question_text }}</p>
          <ul>
            <li v-for="answer in question.answers" :key="answer.answer_id">
              {{ answer.answer_text }}
            </li>
          </ul>
        </div>
        <button @click="closeQuiz" class="btn">Close</button>
      </div>
      
      <div v-if="error" class="error card">
        <h2>Error</h2>
        <p>{{ error }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        quizzes: [],
        selectedQuiz: null,
        error: null,
        userId: 1 // Replace with the actual user ID
      };
    },
    created() {
      this.fetchQuizzes();
    },
    methods: {
      async fetchQuizzes() {
        try {
          const response = await axios.get(`/quiz/${this.userId}`);
          this.quizzes = response.data.quizzes;
          this.error = null;
        } catch (error) {
          this.handleError(error);
        }
      },
      async viewQuiz(QID) {
        try {
          const response = await axios.get(`/quiz/${this.userId}/${QID}`);
          this.selectedQuiz = response.data;
          this.error = null;
        } catch (error) {
          this.handleError(error);
        }
      },
      closeQuiz() {
        this.selectedQuiz = null;
      },
      formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString(undefined, options);
      },
      getImageUrl(image) {
        return new URL(`../assets/images/${image}`, import.meta.url).href;
      },
      handleError(error) {
        console.error('Error:', error);
        if (error.response) {
          this.error = `Server error: ${error.response.data.message || error.response.statusText}`;
        } else if (error.request) {
          this.error = 'No response received from the server. Please check your internet connection and try again.';
        } else {
          this.error = `Error setting up the request: ${error.message}`;
        }
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
  
  .quizzes-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
  }
  
  .quiz-item {
    margin: 10px;
    padding: 20px;
    width: 300px;
  }
  
  .no-quizzes {
    text-align: center;
  }
  
  .quiz-details {
    margin-top: 20px;
    padding: 20px;
  }
  
  .error {
    margin-top: 20px;
    padding: 20px;
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
  
  .question-item {
    margin: 10px 0;
  }
  
  .error p {
    color: red;
  }
  </style>
  