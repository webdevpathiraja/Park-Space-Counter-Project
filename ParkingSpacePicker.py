import cv2
import pickle

# width = 157-50, height = 240-192
width, height = 107, 48
positionList = []


def mouseclick(events, x, y, flags, params):

    # left-click to select a parking space
    if events == cv2.EVENT_LBUTTONDOWN:
        positionList.append((x, y))

    # right-click to remove a selected parking space
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, position in enumerate(positionList):
            x1, y1 = position
            if x1 < x < x1 + width and y1 < y < y1 + height:
                positionList.pop(i)


while True:
    img = cv2.imread('carParkImg.png')

    for position in positionList:
        cv2.rectangle(img, position, (position[0] + width, position[1] + height), (255, 0, 255), 2)

    cv2.imshow("Car Park", img)
    cv2.setMouseCallback("Car Park", mouseclick)
    cv2.waitKey(1)
