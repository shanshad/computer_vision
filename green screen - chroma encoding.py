# # Process Flow
# ---------------
# first take foreground image. since it is a green screen image , we will filter out the green color. for that convert the image to hsv
# and find the lower and upper limits of green color. later compare each pixels of the image to check if it is in betwwen the thresholds of
# colour green , if so mark its position as false (will come in handy later) else mark its position as true.store this individual pixel true or false
# value in an array called mask.now multiply original foreground image with created mask, which will result in all the green pixel turning to zero (black)
# and other pixels will stay as it is.and as a result, we will be getting a cropped image
#
# now make sure the foreground image and background image are of same dimension,if not create a padding of the size of large image and place the smaller
# image in that. after this just add the images and divide the result by two


import cv2
import numpy as np
from esc import get_bounds
import matplotlib.pyplot as plt

def image_addition(im1,im2):
    if im1.shape != im2.shape:
        print('shape mismatch')
        exit()
    else:
        pfinal=im1.astype(np.int32)+im2.astype(np.int32) #the default data type is int8 , which means if i add 100+200 it will give 44 (300-256). so i am converting my data into larger data type to prevent the wrap around
        clipped=np.clip(pfinal,0,255)
        final=clipped/2
        final=final.astype(np.uint8)
        return final


def inrange(img,lower,upper):
    #in this function i will compare each pixel from img falls in between lower and upper limit (ie green pixel or not)
    #if it is a green pixel i will add its value as False in the new mask matrix
    #else i will add True in the mask matrix
    #so the mask matrix will consist of True or False values with same shape of original image
    #so if i multiply (element wise) this mask to foreground, all the green pixel will be multiplied with 0 and will turn to black (0)
    #other pixels will be the same
    #then we can add both fore ground and background
    masc=np.zeros((img.shape[0],img.shape[1],1),np.uint8)
    lower=tuple(lower)
    upper=tuple(upper)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            k=tuple(img[i][j])
            if k > lower and k < upper:
                masc[i][j]=False
            else:
                masc[i][j]=True
    return masc #now all green pixels turned into zero and non green pixels turned to 1 that means only batman figure positions (or that particular pixel with rgb values) are 1


green=[0,255,0]#BGR code for green
fg=cv2.imread('batman.jpg')
bg=cv2.imread('bg1.jpg')
lower,upper=get_bounds(green)
hsv=cv2.cvtColor(fg,cv2.COLOR_BGR2HSV)
mask=inrange(hsv,lower,upper)
print(mask.shape)
p,c=np.unique(mask,return_counts=True)
# plt.bar(p,c)# here 255 is greenscreen and 0 is batman
# plt.show()

fg=fg*mask
# cv2.imshow('fg',fg) #uncommrnt this and run to see the cropped image
padding=np.zeros_like(bg)
h_fg=fg.shape[0]
w_fg=fg.shape[1]
m_h=round(((bg.shape[0])/2))
m_w=round(((bg.shape[1])/2))
padding[0:h_fg,0:w_fg]=fg
# padding[m_h:(h_fg+m_h),m_w:(w_fg+m_w)]=fg #testing by placing it in the middle of picture
# cv2.imshow('padded foreground',padding)
final=image_addition(bg,padding)

cv2.imshow('final image',final)
cv2.waitKey(0)
