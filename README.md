# 🚍⛳ Parking Space Counter 🚕⛳

## Overview  
This project is a real-time **Parking Space Detection & Counter System** that processes video feeds to determine available and occupied parking spots using **OpenCV** and image processing techniques. It provides an efficient, lightweight solution without relying on pre-trained machine learning models.  

## Features  
⭕ **Real-time parking space detection** from a video feed  
⭕ **Adaptive thresholding & contour detection** for accurate space identification 

⭕ **Live counter** displaying available parking slots  
⭕ **Color-coded visualization**:  
   - ❌ **Red** – Occupied  
   - ✅ **Green** – Available  


## 👷🏽‍♀️ Technologies Used 🪜
- **Python** (Core programming language for this project.) 
- **OpenCV** (Handles real-time video processing and image analysis.)
- **NumPy** (Optimizes numerical operations for better efficiency.)
- **cvZone** (Enhances image processing and real-time object detection.)  
- **Pickle** ( Stores and loads predefined parking space positions.)  

## Installation  
### Prerequisites  
Ensure you have **Python** installed, then install dependencies:  
```sh
pip install opencv-python numpy cvzone
```  

## ⭕ Usage  
1️⃣ Place your **parking lot video file** in the project directory.  
2️⃣ Mark parking spaces using the provided interface.  
3️⃣ Run the script:  
   ```sh
   python main.py
   ```  
4️⃣ The system will **process the video & display real-time parking occupancy**.  
5️⃣ Press **`q`** to exit the program.  

## Future Improvements 🔥
🚀 **Deep Learning Integration** – Implementing CNNs for enhanced accuracy.
🚀 **Number Plate Recognition** – Automating reserved spot detection. 
🚀 **Raspberry Pi Deployment** – Enabling efficient real-time processing.
🚀 **Live Camera Feed Support** – Moving beyond pre-recorded videos for real-time security system integration.
 
