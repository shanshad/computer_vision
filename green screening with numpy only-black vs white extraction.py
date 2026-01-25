# this is an attempt to recreate green screen image to other background using numpy only
#here my foreground image contains black coloured batman so i am using black vs white pixel seperation and extraction
#only for this case it will work (with certain flaws)
#since batmans face and eyes are of white/light coloured it was also removed in the cropping process

import cv2
import numpy as np
import matplotlib.pyplot as plt


fg=cv2.imread('batman.jpg')
bg=cv2.imread('bg1.jpg')


gray=cv2.cvtColor(fg,cv2.COLOR_BGR2GRAY) #to find threshold
pixels,count=np.unique(gray,return_counts=True)
plt.bar(pixels,count)#we can see most of the bright pixels are in 150 range
plt.show()
threshold=150#so thresholld value
dude=np.zeros_like(fg)
mask=gray<threshold
dude[mask]=fg[mask]#to extract non green object
cv2.imshow('dude',dude)


padd=np.zeros((bg.shape[0],bg.shape[1],3),dtype=int)#since foreground and background images are of different sizes, padding is required for foreground image
h_fg,w_fg=fg.shape[0],fg.shape[1]
padd[0:h_fg,0:w_fg]=dude #placing the cutout figure from green screen to new big background
padd=padd.astype(np.uint8)
# cv2.imshow('fg',padd)
cv2.waitKey(0)
final=(padd.astype(np.float32)+bg.astype(np.float32))/2 # adding to images and using divided by two to get the final image
final=final.astype(np.uint8)
cv2.imshow('final',final)
cv2.waitKey(0)
