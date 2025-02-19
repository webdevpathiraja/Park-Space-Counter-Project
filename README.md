# Parking Space Counter

## Overview
This project is a parking space detection and counter system that processes a video feed to determine available and occupied parking spots using OpenCV and image processing techniques.

## Features
- Reads a video feed to detect parking spaces.
- Uses adaptive thresholding and morphological operations for accurate space detection.
- Highlights occupied and available parking spaces with different colors.
- Displays a live count of available spaces.

## Technologies Used
- Python
- OpenCV
- NumPy
- cvzone
- Pickle (for storing parking space positions)

## Installation
### Prerequisites
Ensure you have Python installed. Then, install the required dependencies:
```sh
pip install opencv-python numpy cvzone
```

## Usage
1. Place your parking lot video file in the project directory.
2. Mark parking spaces using the provided interface.
3. Run the script:
   ```sh
   python main.py
   ```
4. The system will process the video and display real-time parking occupancy.
5. Press `q` to exit the program.

## Future Improvements
- Enhance detection accuracy with machine learning models.
- Support for real-time camera feeds.

