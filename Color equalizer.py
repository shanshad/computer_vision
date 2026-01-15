import cv2
import matplotlib.pyplot as plt
import numpy as np
fig,(ax1,ax2)=plt.subplots(1,2)
cap=cv2.VideoCapture(0)
ret,frame=cap.read()
if not ret:
    raise IOError("could not read the image")
else:
    webcam_image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    ax1.imshow(webcam_image)
    ax1.axis('off')
    ax1.set_title('before colour equalizing')

    dst_red=cv2.equalizeHist(webcam_image[:,:,0])
    dst_green=cv2.equalizeHist(webcam_image[:,:,1])
    dst_blue=cv2.equalizeHist(webcam_image[:,:,2])
    balanced=webcam_image.copy()
    balanced[:,:,0]=dst_red
    balanced[:,:,1]=dst_green
    balanced[:,:,2]=dst_blue

    ax2.imshow(balanced)
    ax2.axis('off')
    ax2.set_title('after colour equalizing')
    plt.show()