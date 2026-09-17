# Real-Time-Emotion-Detection-and-Analysis-
A Python-based Artificial Intelligence and Computer Vision project that detects human emotions from facial expressions in real time using a webcam. The system uses OpenCV for video processing, FER for emotion recognition, and MTCNN for face detection. It also records emotion data with timestamps and generates an Excel report for further analysis.

**Project Overview**

The application captures live video through a webcam, detects faces, analyzes facial expressions, and displays the dominant emotion along with its confidence score. Emotion data is logged periodically and exported to an Excel file when the application is closed.

**✨ Features**

 Real-time webcam video capture.
 Facial emotion detection using FER.
 Face detection using MTCNN.
 Displays the dominant emotion and confidence score.
 Draws a bounding box around the detected face.
 Records emotion data with timestamps.
 Automatically generates Excel reports.
 Simple Python-based implementation.

**🧠 Emotions Detected**

The system recognizes the following emotions:

Happy, 
Sad, 
Angry, 
Fear, 
Surprise, 
Disgust, 
Neutral.

**🛠️ Technologies Used**

1.Technology	Purpose. 
2.Python	Programming language. 
3.OpenCV	Webcam access and image processing. 
4.FER	Facial emotion recognition. 
5.MTCNN	Face detection. 
6.Pandas	Data storage and processing. 
7.OpenPyXL	Excel report generation.

**⚙️ How It Works**

Webcam Input --> Capture Video Frames --> Convert BGR to RGB --> Detect Face using MTCNN --> Recognize Emotion using FER --> Display Emotion & Confidence --> Store Emotion Data --> Generate Excel Report

**🖥️ Usage**

Connect a working webcam to your computer.
Run the Python program.
Allow the application to access the webcam.
Show your facial expressions in front of the camera.
View the detected emotion and confidence score on the screen.
Press Q while the camera window is active to exit.
The emotion report will be saved as an Excel file.

**📊 Excel Report**

After the session ends, the application generates an Excel report containing:

Timestamp, 
Dominant Emotion, 
Happy Score, 
Sad Score, 
Angry Score, 
Fear Score, 
Surprise Score, 
Disgust Score, 
Neutral Score.

These records can be opened in Microsoft Excel for further analysis of emotional patterns and trends.

