import numpy as np
import sys
import cv2
import matplotlib.pyplot as plt


BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (1.,1.,1.)

cap = cv2.VideoCapture(0)

ret = True
# while ret:
ret, frame = cap.read()
frame = cv2.imread("yy.jpg")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)
contour_info = []
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
for c in contours:
    contour_info.append((
        c,
        cv2.isContourConvex(c),
        cv2.contourArea(c),
    ))
contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
max_contour = contour_info[0]
mask = np.zeros(edges.shape)
cv2.fillConvexPoly(mask, max_contour[0], (255))
mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
mask_stack = np.dstack([mask]*3)
mask_stack  = mask_stack.astype('float32') / 255.0
# img         = img.astype('float32') / 255.0 
masked = (mask_stack * frame)
masked = (masked * 255).astype('uint8')
# _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# contours = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# newimg = cv2.drawContours(frame, contours[0], -1, (0, 255, 0), 2)
# print(type(contours[1]))

cv2.imshow('frame', edges)
cv2.waitKey(0)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break
cap.release()
cv2.destroyAllWindows()