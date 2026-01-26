# Defines a function that takes **one color in BGR format** as input.
# The goal of this function is to compute **HSV lower and upper bounds** for that color so it can be detected in an image.

import numpy as np
import cv2
def get_bounds(colors):
    c=np.uint8([[colors]])
    hsv_c=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    lower_limit=hsv_c[0][0][0] -10,100,100
    upper_limit=hsv_c[0][0][0]+10,255,255
    lower=np.array(lower_limit,np.uint32)
    upper=np.array(upper_limit,np.uint32)
    return lower,upper

