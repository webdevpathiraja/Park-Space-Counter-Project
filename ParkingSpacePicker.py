import cv2
import pickle

img = cv2.imread('carParkImg.png')

# width = 157-50, height = 240-192
width, height = 107, 48
positionList = []


def mouseclick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        positionList.append((x, y))


while True:

    for position in positionList:
        cv2.rectangle(img, position, (position[0] + width, position[1] + height), (255, 0, 255), 2)

    cv2.imshow("Car Park", img)
    cv2.setMouseCallback("Car Park", mouseclick)
    cv2.waitKey(1)
