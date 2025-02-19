import cv2
import pickle

img = cv2.imread('carParkImg.png')

# width = 157-50, height = 240-192
width, height = 107, 48

while True:

    # drawing a rectangle on the image using OpenCV.
    # img – The image on which the rectangle is drawn.
    # The top-left corner of the rectangle (x=50, y=192).
    # The bottom-right corner of the rectangle (x=157, y=240).
    # The color of the rectangle in BGR format (Purple).
    # The thickness of the rectangle's border (2 pixels).
    # cv2.rectangle(img, (50, 192), (157, 240), (255, 0, 255), 2)

    cv2.imshow("Car Park", img)
    cv2.waitKey(1)
