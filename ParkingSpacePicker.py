import cv2
import pickle

img = cv2.imread('carParkImg.png')

while True:
    cv2.imshow("Car Park", img)
    cv2.waitKey(1)
