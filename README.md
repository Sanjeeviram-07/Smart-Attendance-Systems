# 🎯 Smart Attendance System

A modern, AI-powered attendance tracking system that uses facial recognition technology to automatically monitor and manage attendance in real-time.

## ✨ Features

### 🔐 **Authentication & Security**
- **Role-based access control** (Admin/User roles)
- Secure Firebase Authentication
- User registration and login system
- Password reset functionality

### 📸 **Face Recognition**
- **Real-time facial recognition** using webcam
- **OpenCV** and **face_recognition** library integration
- Pre-loaded dataset of known faces
- Automatic attendance marking when faces are recognized
- **Duplicate prevention** - prevents multiple entries for the same person within 30 seconds

### 📊 **Attendance Management**
- **Real-time attendance tracking** with timestamps
- **Date-based filtering** and viewing
- **Excel export functionality** for attendance reports
- **Daily attendance limits** - one entry per person per day
- **Manual entry support** for corrections

### 🎥 **Live Camera Interface**
- **Real-time video feed** with face detection
- **Visual feedback** showing recognized faces with status:
  - 🟢 Green: Not marked yet
  - 🔴 Red: Already marked today
  - ✅ Green: Just marked
- **Performance optimization** (processes every 3rd frame)

## 🏗️ Architecture

```
smart-attendance/
├── backend/                 # Python backend with face recognition
│   ├── main.py             # Main face recognition application
│   ├── check_attendance.py # Attendance checking utilities
│   ├── firebase_config.py  # Firebase configuration
│   ├── user_management.py  # User management functions
│   └── dataset/            # Face images for recognition
├── frontend/               # React frontend application
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.js         # Main application
│   │   └── firebase.js    # Firebase configuration
│   └── package.json       # Dependencies
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Node.js 16+**
- **Webcam** for face recognition
- **Firebase project** with Firestore enabled

### 1. Clone the Repository

```bash
git clone <repository-url>
cd smart-attendance
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your Firebase service account key
# Download serviceAccountKey.json from Firebase Console
# Place it in the backend/ directory

# Add face images to dataset/ folder
# Format: "Person Name.jpg" (e.g., "John Doe.jpg")
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Configure Firebase
# Update src/firebase.js with your Firebase config
```

### 4. Run the Application

#### Backend (Face Recognition)
```bash
cd backend
python main.py
```

#### Frontend (Web Dashboard)
```bash
cd frontend
npm start
```

## 🔧 Configuration

### Firebase Setup

1. **Create a Firebase project** at [Firebase Console](https://console.firebase.google.com/)
2. **Enable Firestore Database**
3. **Enable Authentication** with Email/Password
4. **Download service account key** and save as `serviceAccountKey.json`
5. **Update frontend Firebase config** in `src/firebase.js`

### Face Dataset

1. **Add face images** to `backend/dataset/` folder
2. **Naming convention**: `Person Name.jpg` (e.g., `John Doe.jpg`)
3. **Image requirements**:
   - Clear, front-facing photos
   - Good lighting
   - JPG, PNG, or JPEG format
   - Recommended size: 2-5MB

## 📱 Usage

### Admin Dashboard

- **View real-time attendance** for any date
- **Manage users** (create, delete, assign roles)
- **Export attendance data** to Excel
- **Monitor system status**

### Face Recognition

1. **Start the backend** (`python main.py`)
2. **Position yourself** in front of the webcam
3. **Wait for recognition** - system will automatically mark attendance
4. **Check status** on the live video feed

### Attendance Reports

- **Real-time updates** in the dashboard
- **Date filtering** for historical data
- **Excel export** for analysis and record-keeping

## 🛠️ API Endpoints

### Backend Routes

- **Face Recognition**: Real-time camera feed processing
- **Attendance Storage**: Automatic Firebase Firestore updates
- **User Management**: Firebase Auth integration

### Frontend Routes

- `/` - Login page
- `/register` - User registration
- `/dashboard` - Admin dashboard (protected)
- `/user-dashboard` - User dashboard (protected)

## 🔒 Security Features

- **Role-based access control**
- **Protected routes** for sensitive operations
- **Firebase security rules** for database access
- **Authentication required** for all dashboard access
- **Secure user management** with proper validation

## 📊 Database Schema

### Attendance Collection
```json
{
  "name": "string",
  "time": "HH:MM:SS",
  "date": "YYYY-MM-DD",
  "timestamp": "ISO timestamp",
  "email": "string (optional)",
  "manual_entry": "boolean"
}
```

### Users Collection
```json
{
  "uid": "string",
  "email": "string",
  "role": "admin|user",
  "createdAt": "ISO timestamp"
}
```

## 🚨 Troubleshooting

### Common Issues

1. **Camera not working**
   - Check webcam permissions
   - Ensure no other application is using the camera

2. **Face recognition not working**
   - Verify face images are in the dataset folder
   - Check image quality and lighting
   - Ensure proper naming convention

3. **Firebase connection errors**
   - Verify `serviceAccountKey.json` is in the backend directory
   - Check Firebase project configuration
   - Ensure Firestore is enabled

4. **Frontend build errors**
   - Clear `node_modules` and reinstall
   - Check Node.js version compatibility

### Performance Tips

- **Reduce image resolution** for better performance
- **Limit dataset size** to essential faces only
- **Use SSD storage** for faster image loading
- **Optimize lighting** for better recognition accuracy

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV** for computer vision capabilities
- **face_recognition** library for facial recognition
- **Firebase** for backend services
- **React** for the frontend framework

## 📞 Support

For support and questions:
- **Create an issue** in the repository
- **Check the troubleshooting** section above
- **Review Firebase documentation** for configuration issues

---

**Made with ❤️ for efficient attendance management**
