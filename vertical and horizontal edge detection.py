# process flow
# image -> gray -> binary -> row wise and column wise gradient -> find vertical edge,horizontal edge -> sum


import numpy as np
import cv2
import matplotlib.pyplot as plt


def binary(img,threshold):
    binary=np.zeros((img.shape[0],img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] < threshold:
                binary[i,j]=255
            else:
                binary[i,j]=0
    return binary

def vertical_edge_detection(binary):
    vertical=np.zeros_like(binary)
    for i in range(binary.shape[0]):
        for j in range(binary.shape[1]-1):
            if binary[i,j] != binary[i,j+1]:
                vertical[i,j+1]=True
            else:
                vertical[i,j+1]=False
    return vertical

def horizontal_edge_detection(binary):
    horizontal=np.zeros_like(binary)
    for i in range(binary.shape[1]-1):
        for j in range(binary.shape[0]):
            if binary[i,j] != binary[i+1,j]:
                horizontal[i+1,j]=True
            else:
                horizontal[j,i+1]=False
    return horizontal

def additon(im1,im2):
    new=(im1*255+im2*255).astype(np.uint8)
    return new
image=cv2.imread('pi.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.equalizeHist(gray)
pixels,counts=np.unique(gray,return_counts=True)
# plt.bar(pixels,counts)
# plt.show()
binary=binary(gray,6)
dilat=cv2.dilate(binary,(7,7),iterations=2)
binary_clear=cv2.erode(dilat,(7,7),iterations=2)
vertical_edge=vertical_edge_detection(binary_clear)
horizontal_edge=horizontal_edge_detection(binary_clear)
cv2.imshow("binary",binary_clear)
cv2.imshow("horizontal",horizontal_edge)
cv2.imshow("vertical",vertical_edge)
sum=additon(vertical_edge,horizontal_edge)
# sum=sum.astype(np.uint8)
cv2.imshow("sum",sum)
cv2.waitKey(0)
cv2.destroyAllWindows()