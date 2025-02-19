import cv2
import pickle

# Video feed (using forward slashes)
capture = cv2.VideoCapture('C:/Users/ACER/Documents/GitHub/Park-Space-Counter-Project/carPark.mp4')

with open('CarParkPosition', 'rb') as f:
    positionList = pickle.load(f)

width, height = 107, 48

def checkParkingSpace():
    for position in positionList:
        x, y = position


        imgCrop = img[y: y + height, x: x + width]
        cv2.imshow(str(x*y), imgCrop)



# Check if the video was opened correctly
if not capture.isOpened():
    print("Error: Unable to open video file.")
    exit()

while True:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = capture.read()
    checkParkingSpace()

    for position in positionList:
        cv2.rectangle(img, position, (position[0] + width, position[1] + height), (255, 0, 255), 2)




    # Check if the frame is successfully captured
    if not success:
        print("Error: Failed to capture image.")
        break

    cv2.imshow("Car Park", img)

    # Wait for key press to exit
    if cv2.waitKey(10) & 0xFF == ord('q'):  # Press 'q' to exit
        break

capture.release()
cv2.destroyAllWindows()