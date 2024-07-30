import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import MoodTracker from '../views/MoodTracker.vue';
import GoalSetting from '../views/Goalsetter.vue';
import Journal from '../views/Journal.vue';
import Meditation from '../views/Meditation.vue';
import SymptomCheck from '../views/SymptomCheck.vue';
import Chat from '../views/Chat.vue';
import TitlePage from '../views/TitlePage.vue';
import CreateProfile from '../views/CreateProfile.vue';
import SignIn from '../views/Signin.vue';
import SignupVerification from '../views/SignupVerification.vue';
import Quiz from '../views/Quiz.vue';
import Helpline from '@/views/Helpline.vue';

const routes = [
  { path: '/', component: TitlePage },
  { path: '/moodtracker', component: MoodTracker },
  { path: '/goalsetter', component: GoalSetting },
  { path: '/journal', component: Journal },
  { path: '/meditation', component: Meditation },
  { path: '/symptomcheck', component: SymptomCheck },
  { path: '/chat', component: Chat },
  { path: '/home', name: 'Home', component: Home },
  { path: '/signup', name: 'CreateProfile', component: CreateProfile },
  { path: '/signin', name: 'SignIn', component: SignIn },
  { path: '/signupverification', name: 'SignupVerification', component: SignupVerification },
  { path: '/quiz', name: 'Quiz', component: Quiz },
  { path: '/helpline', name: 'Helplines', component: Helpline }
];

const router = createRouter({
   history: createWebHistory(),
  routes
});

export default router;
