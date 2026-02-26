# 🔐 AI-Based Smart Intruder Detection System

An AI-powered real-time security system that detects human presence using computer vision, recognizes authorized faces, and automatically captures intruder images with timestamps.

---

## 🚀 Project Overview

This project uses **YOLOv8** for real-time person detection and **face recognition** to verify identities from a live camera feed.  
If an unknown person is detected, the system raises an alert and saves the intruder’s image for evidence.

The project is designed with a **hybrid architecture**:
- Local system for real-time camera access
- Cloud deployment (Render) for backend and API demonstration

---

## 🧠 How It Works

1. Capture live video from webcam
2. Detect humans using YOLOv8
3. Extract and encode detected faces
4. Compare with known face encodings
5. If face is unknown:
   - Display alert on screen
   - Save intruder image with timestamp

---

## ✨ Features

- Real-time human detection
- Face recognition for authorized users
- Automatic intruder image capture
- Timestamped evidence storage
- Dockerized for portability
- Clean and modular code structure

---

## 🛠️ Tech Stack

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- Face Recognition (dlib)
- NumPy
- Docker
- Render (Cloud Deployment)

---

## 📁 Project Structure

```text
Security-Intruder-Detection/
│── main.py
│── Dockerfile
│── requirements.txt
│── README.md
│── known_faces/
│── utils/
│   └── tracker.py
│── intruders/
