import cv2
import os
import face_recognition
from datetime import datetime
from firebase_config import db

path = 'dataset'
images = []
names = []

# Load known faces
for file in os.listdir(path):
    if file.lower().endswith(('.jpg', '.png', '.jpeg')):
        img = face_recognition.load_image_file(f'{path}/{file}')
        encode = face_recognition.face_encodings(img)
        if encode:
            images.append(encode[0])
            names.append(os.path.splitext(file)[0])
        else:
            print(f"⚠️ No face found in image: {file}")

# Auto-detect a working webcam
def find_camera_index():
    for index in range(5):
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            print(f"✅ Webcam found at index: {index}")
            cap.release()
            return index
        cap.release()
    print("❌ No working webcam found.")
    return -1

camera_index = find_camera_index()
if camera_index == -1:
    exit()

cap = cv2.VideoCapture(camera_index)
if not cap.isOpened():
    print("❌ Could not open webcam.")
    exit()

attendance = []

# Attendance capture loop
while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("❌ Failed to grab frame.")
        continue

    small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    for encoding, loc in zip(encodings, locations):
        if not images:
            continue
        matches = face_recognition.compare_faces(images, encoding)
        dist = face_recognition.face_distance(images, encoding)
        if len(dist) == 0:
            continue
        best = dist.argmin()
        if dist[best] < 0.45:  # Adjust this threshold (lower = more strict)
            name = names[best]
            if name not in attendance:
                attendance.append(name)
                now = datetime.now()
                time = now.strftime('%H:%M:%S')
                date = now.strftime('%Y-%m-%d')
                db.collection("attendance").add({
                    "name": name,
                    "time": time,
                    "date": date
                })

                print(f"✅ {name} marked present at {date}, {time}")

            top, right, bottom, left = [v * 4 for v in loc]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Quitting webcam feed.")
        break

cap.release()
cv2.destroyAllWindows()
