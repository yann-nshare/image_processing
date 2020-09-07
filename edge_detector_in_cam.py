import numpy as np
import sys
import cv2
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)

ret = True
while ret:
    ret, frame = cap.read()
    # frame = cv2.imread("yy.jpg")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(gray, (5, 5), 3)
    _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    contours = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    newimg = cv2.drawContours(gray, contours[0], -1, (0, 255, 0), 2)

    cv2.imshow('frame', newimg)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
