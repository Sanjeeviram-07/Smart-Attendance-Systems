import React, { useEffect, useState } from 'react';
import { db } from '../firebase';
import { collection, getDocs } from 'firebase/firestore';
import { motion } from 'framer-motion';
import './Dashboard.css';

function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const querySnapshot = await getDocs(collection(db, 'attendance'));
      const docs = querySnapshot.docs.map(doc => doc.data());
      setData(docs);
    };
    fetchData();
  }, []);

  return (
    <motion.div className="dashboard-container" initial={{ y: 50, opacity: 0 }} animate={{ y: 0, opacity: 1 }}>
      <h1>Attendance Dashboard</h1>
      <div className="glass-table">
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Date</th>
              <th>Time</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={index}>
                <td>{item.name}</td>
                <td>{item.date}</td>
                <td>{item.time}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </motion.div>
  );
}

export default Dashboard;