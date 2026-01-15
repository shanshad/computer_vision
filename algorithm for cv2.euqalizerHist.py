import numpy as np
import cv2
import matplotlib.pyplot as plt
L=256
cap=cv2.VideoCapture(0)
ret, before=cap.read()
cp=before.copy()
cv2.imshow('before',before)
# print(before.shape)
gray=cv2.cvtColor(before,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
# print(f'before image min = {np.min(before)}, max = {np.max(before)} , std = {np.std(before)}')
# print(f'gray image min = {np.min(gray)}, max = {np.max(gray)} , std = {np.std(gray)}')
# plt.hist(gray, bins=[i for i in range(256)])
# plt.show()
pixel,count=np.unique(gray,return_counts=True)
# print(pixel,count)
# plt.bar(pixel,count)
no_pixels=np.sum(count)
# print('no of pixels:',no_pixels)
prob=[]
# print(len(pixel),len(count))
histc=np.zeros(256,dtype=int)#for creating a list of length 256 which contains no of counts in respective pixel value position
for i in range(len(pixel)):
    histc[pixel[i]]=count[i]
# print(histc)
for i in range(256):
    prob.append(histc[i]/no_pixels) #probability of each pixel value
pdf=np.array(prob)
cdf=np.cumsum(pdf) #cumulative sum
mapping=np.round((L-1)*cdf).astype(np.uint8) #formula (L-1)*cumulative sum, it returns a list of length 256 values ranging from 0 to 255
# print(mapping)
equalized=mapping[cp] #mapping[k] tells you: “If your pixel value is k, change it to mapping[k] Example: mapping[50] = 120 → any pixel that was 50 becomes 120 mapping[200] = 220 → any pixel that was 200 becomes 220
cv2.imshow('equalized',equalized)
# back=cv2.cvtColor(equalized,cv2.COLOR_GRAY2RGB)
# cv2.imshow('equalized',back)
# plt.show()
cv2.waitKey(0)
