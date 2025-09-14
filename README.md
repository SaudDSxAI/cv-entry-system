# Access Vision: Computer Vision Entry System

Welcome to Access Vision! This project documents my journey in building a computer vision-based entry and exit management system for institutions. The system integrates face recognition, sensor data, real-time visualization, and automated data logging to streamline and secure access control.

## Project Overview
- **Goal:** Automate and monitor entry/exit of individuals using face recognition and sensor data.
- **Technologies:** Python, OpenCV, face_recognition, pywinauto, pandas, matplotlib
- **Key Features:**
  - Real-time face recognition using camera feeds
  - Integration with ultrasonic sensors via serial communication
  - Automated logging of entry/exit events to CSV
  - Data visualization of access patterns
  - GUI automation for serial terminal control

## System Components
- **recognizer.py:** Face encoding and recognition logic
- **capture.py:** Camera capture, face detection, and data extraction
- **in_out.py:** Main workflow for reading sensor data, triggering recognition, logging events, and visualization
- **visual.py:** Real-time visualization of entry/exit data
- **Students_Data.csv:** Stores all access records for analysis

## How It Works
1. The system listens for sensor triggers (Entry/Exit) via a serial terminal (CoolTerm).
2. On trigger, it captures a face image, recognizes the individual, and logs the event (name, reg number, time, date, batch, faculty).
3. All events are appended to a CSV file for record-keeping.
4. Real-time bar charts visualize the number of entries and exits per student.

## Key Learnings & Challenges
- Integrating hardware (sensors) with software workflows
- Real-time face recognition and handling unknown faces
- Automating GUI interactions for serial communication
- Ensuring robust data logging and visualization
- Troubleshooting camera, sensor, and file I/O issues

## How to Run
1. Install required packages:
   ```bash
   pip install opencv-python face_recognition pywinauto pandas matplotlib
   ```
2. Update file paths as needed in the scripts.
3. Connect cameras and sensors, and start the serial terminal (CoolTerm).
4. Run `in_out.py` to launch the system.

## About This Project
This project reflects my hands-on struggle and growth in computer vision, hardware integration, and real-time data analysis. It demonstrates a complete workflow from sensor input to actionable insights.

---

Thank you for exploring Access Vision!
