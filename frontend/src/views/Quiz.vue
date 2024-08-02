<template>
  <div class="quiz container">
    <header>
      <h1>Quiz</h1>
      <img :src="getImageUrl('quizbot.png')" alt="Avatar" class="avatar">
    </header>
     <!-- Display list of available quizzes -->
    <div v-if="quizzes.length" class="quizzes-list">
      <div v-for="quiz in quizzes" :key="quiz.QID" class="quiz-item card">
          <!-- Display quiz ID and date -->
        <h2>Quiz ID: {{ quiz.QID }}</h2>
        <p>Date: {{ formatDate(quiz.quiz_date) }}</p>
          <!-- Button to start a selected quiz -->
        <button @click="viewQuiz(quiz.QID)" class="btn">Take Quiz</button>
      </div>
    </div>
      <!-- Message for when no quizzes are available -->
    <div v-else class="no-quizzes card">
      <h2>No Quizzes Found</h2>
      <p>You have no quizzes available.</p>
    </div>
      <!-- Display quiz details when a quiz is selected -->
    <div v-if="selectedQuiz" class="quiz-details card">
      <h2>Quiz Details</h2>
      <form @submit.prevent="submitQuiz">
           <!-- Loop through questions in the selected quiz -->
        <div v-for="question in selectedQuiz.questions" :key="question.question_id" class="question-item">
             <!-- Display question text -->
          <p>{{ question.question_text }}</p>
          <ul>
              <!-- Loop through possible answers for the question -->
            <li v-for="answer in question.answers" :key="answer.answer_id">
               <!-- Radio button for each answer option -->
              <input
                type="radio"
                :name="'question-' + question.question_id"
                :value="answer.answer_id"
                v-model="selectedAnswers[question.question_id]"
              />
              {{ answer.answer_text }}
            </li>
          </ul>
        </div>
         <!-- Submit button for the quiz -->
        <button type="submit" class="btn">Submit Quiz</button>
      </form>
       <!-- Button to close the quiz details view -->
      <button @click="closeQuiz" class="btn">Close</button>
    </div>

     <!-- Display error message if there is an error -->
    <div v-if="error" class="error card">
      <h2>Error</h2>
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // Sample quiz data with questions and answers

      quizzes: [
        {
          QID: 1,
          quiz_date: '2024-01-01',
          questions: [
            {
              question_id: 1,
              question_text: 'How often have you been bothered by feeling down, depressed, or hopeless over the past two weeks?',
              answers: [
                { answer_id: 1, answer_text: 'Not at all' },
                { answer_id: 2, answer_text: 'Several days' },
                { answer_id: 3, answer_text: 'More than half the days' },
                { answer_id: 4, answer_text: 'Nearly every day' }
              ]
            },
            {
              question_id: 2,
              question_text: 'How often have you had little interest or pleasure in doing things over the past two weeks?',
              answers: [
                { answer_id: 5, answer_text: 'Not at all' },
                { answer_id: 6, answer_text: 'Several days' },
                { answer_id: 7, answer_text: 'More than half the days' },
                { answer_id: 8, answer_text: 'Nearly every day' }
              ]
            }
          ]
        },
        {
          QID: 2,
          quiz_date: '2024-01-02',
          questions: [
            {
              question_id: 3,
              question_text: 'Over the last month, how often have you felt nervous, anxious, or on edge?',
              answers: [
                { answer_id: 9, answer_text: 'Not at all' },
                { answer_id: 10, answer_text: 'Several days' },
                { answer_id: 11, answer_text: 'More than half the days' },
                { answer_id: 12, answer_text: 'Nearly every day' }
              ]
            },
            {
              question_id: 4,
              question_text: 'Over the last month, how often have you been unable to stop or control worrying?',
              answers: [
                { answer_id: 13, answer_text: 'Not at all' },
                { answer_id: 14, answer_text: 'Several days' },
                { answer_id: 15, answer_text: 'More than half the days' },
                { answer_id: 16, answer_text: 'Nearly every day' }
              ]
            }
          ]
        }
      ],
      selectedQuiz: null, // Currently selected quiz
      selectedAnswers: {}, // Object to store selected answers
      error: null, // Error message if any error occurs
      userId: 1 // Placeholder user ID
    };
  },
  methods: {
     // Method to select and view a quiz based on its ID
    viewQuiz(QID) {
      this.selectedQuiz = this.quizzes.find(quiz => quiz.QID === QID);
      this.selectedAnswers = {};
      this.error = null;
    },
      // Method to handle quiz submission
    submitQuiz() {
      const answers = Object.entries(this.selectedAnswers).map(([questionId, answerId]) => ({
        questionId,
        answerId
      }));
      console.log('User submitted answers:', answers);
      alert('Quiz submitted successfully!');
      this.selectedQuiz = null; // Clear selected quiz after submission
    },
     // Method to close the quiz details view
    closeQuiz() {
      this.selectedQuiz = null;
    },
    // Method to format the date into a readable format
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
      // Method to get the URL of an image asset
    getImageUrl(image) {
      return new URL('../assets/images/${image}', import.meta.url).href;
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

.quizzes-list,
.quiz-details,
.no-quizzes,
.error {
  width: 100%;
  max-width: 600px;
  margin: 20px 0;
  background-color: #f5efe6;
  border-radius: 8px;
  padding: 20px;
  box-sizing: border-box;
}

.card {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

header {
  text-align: center;
  margin-bottom: 20px;
}

h1 {
  color: #3c2317;
  font-size: 32px;
  margin: 0;
  font-family: 'Copperplate', 'Papyrus', fantasy;
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

.quiz-item,
.no-quizzes,
.error {
  text-align: center;
}

.question-item {
  margin-bottom: 20px;
}

.btn {
  background-color: #4caf50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn:hover {
  background-color: #45a049;
}

.error {
  color: red;
}
</style>