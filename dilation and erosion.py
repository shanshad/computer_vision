import cv2
import numpy as np
import matplotlib.pyplot as plt

def binary(img,threshold):
    binary=np.zeros((img.shape[0],img.shape[1]),np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            k=img[i][j]
            if k < threshold:
                binary[i][j]=0
            else:
                binary[i][j]=255
    binary=binary.astype(np.uint8)
    return binary

cap=cv2.VideoCapture(0)
ret,frame=cap.read()
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
binary=binary(gray,100)
binary=binary.astype(np.uint8)
cv2.imshow("binary",binary)
dilated=cv2.dilate(binary,(7,7),iterations=2)
eroded=cv2.erode(binary,(7,7),iterations=2)

cv2.imshow("dilated",dilated)
cv2.imshow("eroded",eroded)
cv2.waitKey(0)