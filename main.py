import cv2
import pickle
import numpy as np
import cvzone

# Initialize video feed from the file
capture = cv2.VideoCapture('C:/Users/ACER/Documents/GitHub/Park-Space-Counter-Project/carPark.mp4')

# Load parking space positions from file
with open('CarParkPosition', 'rb') as f:
    positionList = pickle.load(f)

# Set width and height for parking space area
width, height = 107, 48


def checkParkingSpace(imgProcess):
    spaceCounter = 0

    # Loop through each parking space position
    for position in positionList:
        x, y = position

        # Crop the image to the parking space area
        imgCrop = imgProcess[y: y + height, x: x + width]

        # Count non-zero pixels in the cropped image (indicates presence of a car)
        count = cv2.countNonZero(imgCrop)

        # If spot is available (fewer pixels occupied)
        if count < 900:
            color = (0, 220, 0)  # Green color for available space
            thickness = 3
            spaceCounter += 1
        else:  # If spot is not available (more pixels occupied)
            color = (0, 0, 200)  # Red color for occupied space
            thickness = 2

        # Draw rectangle around parking space
        cv2.rectangle(img, position, (position[0] + width, position[1] + height), color, thickness)

        # Display the count of occupied pixels in the parking space
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=1, colorR=color)

    # Display the total count of free parking spaces
    cvzone.putTextRect(img, str(f'AVAILABLE PARKING SLOTS: {spaceCounter}/{len(positionList)}'), (60, 50), scale=0.8,
                       thickness=2, font=cv2.FONT_HERSHEY_SIMPLEX, offset=10, colorR=(0, 190, 250), colorT=(0, 0, 0))


# Check if the video was opened correctly
if not capture.isOpened():
    print("Error: Unable to open video file.")
    exit()

while True:
    # Reset to the first frame once video ends
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = capture.read()

    # Convert image to grayscale and apply Gaussian blur
    imGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    imgBlur = cv2.GaussianBlur(imGray, (3, 3), 1)

    # Apply adaptive thresholding for better image processing
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    # Apply median blur to reduce noise
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.int8)

    # Dilate the image to enhance features
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    # Check parking space availability
    checkParkingSpace(imgDilate)

    # Ensure frame was successfully captured
    if not success:
        print("Error: Failed to capture image.")
        break

    # Display the processed image
    cv2.imshow("Car Park", img)

    # Wait for key press to exit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
capture.release()
cv2.destroyAllWindows()
