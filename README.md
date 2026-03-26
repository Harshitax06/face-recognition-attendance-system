# Face Recognition Attendance System

# Abstract 

The management of the attendance can be a great burden on the teachers if it is done by hand. To resolve this problem, smart and auto attendance management system is being utilized. By utilizing this framework, the problem of proxies and students being marked present even though they are not physically present can easily be solved. This system marks the attendance using live video stream. The frames are extracted from video using OpenCV. The main implementation steps used in this type of system are face detection and recognizing the detected face, for which dlib is used. After these, the connection of recognized faces ought to be conceivable by comparing with the database containing student's faces. This model will be a successful technique to manage the attendance of students.

# Problem Statement
Live Webcam based Face Attendance System Project through python programming and openCv
Manual attendance systems are time-consuming and prone to errors such as proxy attendance. This project aims to automate attendance using face recognition technology.


# Details 

Smart Attendance Management System is an application developed for daily student attendance in colleges or. schools. This project attempts to record attendance through face detection.

This System uses facial recognition technology to record the attendance through a high resolution digital camera/webcam that detects and recognizes faces and compare the recognize faces with students/known faces images stored in faces database(CSV).

# Reference Base Research Paper : https://ieeexplore.ieee.org/document/9215441

# Overview
This project is a face recognition-based attendance system developed using Python and OpenCV. It detects and recognizes faces and marks attendance automatically.

# Features
- Face detection using OpenCV
- Face recognition
- Attendance marking system
- Stores attendance data

# Technologies Used
- Python
- OpenCV
- NumPy
- VS Code

# How It Works
- Captures live video using webcam
- Detects faces using OpenCV
- Encodes faces using face_recognition library
- Matches faces with stored dataset
- Marks attendance in CSV file

# Project Structure
- AttendanceProject.py → Main file
- dataset → Stored images
- encodings → Face encodings

# Installation & Setup

git clone https://github.com/Harshitax06/face-recognition-attendance-system.git

cd face-recognition-attendance-system

pip install -r requirements.txt

python AttendanceProject.py

  

# Output
The system detects faces in real-time and marks attendance automatically in a CSV file with date and time.

# Learning Outcomes
- Learned face recognition concepts
- Worked with OpenCV and Python
- Implemented real-time attendance system





