import cv2
import pickle

# Define width and height of parking space
width, height = 107, 48

try:
    # Load saved parking positions if the file exists
    with open('CarParkPosition', 'rb') as f:
        positionList = pickle.load(f)
except:
    positionList = []  # Initialize an empty list if file doesn't exist or loading fails

def mouseclick(events, x, y, flags, params):
    # Left-click to select a parking space
    if events == cv2.EVENT_LBUTTONDOWN:
        positionList.append((x, y))

    # Right-click to remove a selected parking space
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, position in enumerate(positionList):
            x1, y1 = position
            if x1 < x < x1 + width and y1 < y < y1 + height:
                positionList.pop(i)

    # Save updated positions to the file
    with open('CarParkPosition', 'wb') as f:
        pickle.dump(positionList, f)

while True:
    # Load the car park image
    img = cv2.imread('carParkImg.png')

    # Draw rectangles around selected parking spaces
    for position in positionList:
        cv2.rectangle(img, position, (position[0] + width, position[1] + height), (255, 0, 255), 2)

    # Display the car park image
    cv2.imshow("Car Park", img)

    # Set mouse callback function to handle user clicks
    cv2.setMouseCallback("Car Park", mouseclick)

    # Wait for a key press (1 ms delay)
    cv2.waitKey(1)
