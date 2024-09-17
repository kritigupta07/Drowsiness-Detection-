
# **Wake Wave: A Machine Learning-Based Driver Drowsiness Detection System** 🚗💤

**Project Overview**  
*Wake Wave* is a machine learning-based system designed to enhance road safety by detecting drowsiness in drivers. This project was built entirely from scratch, incorporating cutting-edge machine learning techniques to provide real-time detection and alerts, thereby preventing potential accidents caused by driver fatigue.

Our solution leverages facial landmark analysis, using real-time image processing to monitor driver behavior. By analyzing indicators such as **eye closure**. *Wake Wave* effectively determines drowsiness and sends timely alerts to ensure the driver's safety.

We have also built a **website** showcasing our project, giving users an overview of the system, its implementation, and its real-world application. Additionally, the website features a **GPS system** to track the driver’s location, and we plan to integrate a **speed limit feature** in the near future.

---

## **Key Features**
- **Real-time Monitoring**: Continuously monitors the driver's facial features using a camera and performs real-time analysis.
- **Drowsiness Detection**: Uses facial landmarks to track eye closure and calculates the Eye Aspect Ratio (EAR) to detect when the driver's eyes remain closed for a prolonged period.
- **Alerts**: Immediately notifies the driver through an alert system if drowsiness is detected, preventing potential accidents.
- **GPS Integration**: The website includes a **GPS system** that allows for real-time tracking of the driver's location, adding an extra layer of safety.
- **Future Expansion**: We plan to introduce a **speed limit feature** to monitor the driver's speed and ensure they are adhering to safe driving practices.
- **Machine Learning from Scratch**: We utilized Python, OpenCV, and Keras to build the entire model. The project includes face detection, eye classification, and real-time alerting.
- **Website Integration**: A comprehensive website showcasing the project and its capabilities.

---

## **How It Works**
1. **Image Capture**: The system captures images from a webcam using OpenCV.
2. **Face Detection**: The face is detected, and a Region of Interest (ROI) is created for focused analysis.
3. **Eye Detection**: Eyes are detected within the ROI and analyzed to determine their state (open/closed).
4. **Classification**: A Convolutional Neural Network (CNN) model classifies the eyes’ status based on the Eye Aspect Ratio (EAR).
5. **Alert System**: If the eyes remain closed for a certain duration, the system triggers an alert, signaling drowsiness.
6. **GPS Tracking**: The integrated **GPS system** provides real-time tracking of the driver’s location, enhancing safety by monitoring driving patterns.
7. **Future Features**: A **speed limit feature** will be implemented soon to ensure the driver maintains a safe speed.

---

## **Technical Details**
- **Frameworks Used**:  
  - Python for scripting
  - OpenCV for image processing
  - Keras with Convolutional Neural Networks (CNN) for classification
  - Dlib's pre-trained shape predictor for facial landmark detection
  - Haar cascade classifier for face and eye detection

- **Model Architecture**:  
  Our model is built using a CNN with multiple layers for extracting complex features from the input images. The final output layer uses the **Softmax function** to classify whether the driver is drowsy or alert.

---

## **Results**
The system effectively detects driver drowsiness by monitoring facial cues, with a special focus on eye behavior. It provides timely alerts in real-time scenarios, significantly contributing to road safety.

---

## **Website**
Our website showcases the **Wake Wave** system and its application in preventing accidents caused by drowsiness. Along with an overview of how the detection system works, we have integrated a **GPS system** that allows for real-time location tracking. 

In the future, we plan to introduce a **speed limit monitoring feature**, which will ensure drivers are maintaining safe driving speeds.

---

## **Conclusion**
*Wake Wave* aims to make roads safer by preventing accidents caused by drowsy driving. By utilizing machine learning techniques, facial landmark analysis, **GPS tracking**, and real-time alerts, *Wake Wave* offers a robust solution to a widespread issue. We look forward to further enhancing the system and integrating additional features such as speed limit monitoring for even greater driver safety.

---
