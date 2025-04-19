import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';

const firebaseConfig = {
  apiKey: "AIzaSyDgg75kP3Q76CVKU2-lYgtok_wBcGkX-2c",
  authDomain: "smart-attendance-25d52.firebaseapp.com",
  projectId: "smart-attendance-25d52",
  storageBucket: "smart-attendance-25d52.firebasestorage.app",
  messagingSenderId: "856864480830",
  appId: "1:856864480830:web:2857c1e24a48b6392dbb6f"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);
export { db, auth };