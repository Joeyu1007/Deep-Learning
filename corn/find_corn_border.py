import cv2
import torch
from PIL import Image
import numpy as np
import scipy.misc

# image = Image.open('C:/Users/Adm/Desktop/玉米/bad_res.jpg')
# corn_img = np.array(image)

image = cv2.imread('C:/Users/Adm/Desktop/corn/bad_res.jpg',cv2.IMREAD_GRAYSCALE)
#print(image)

ret,image = cv2.threshold(image,5,255,0)
#image = cv2.Canny(image,50,200)
#print(image)
# g = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# print(g)

h = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#提取轮廓
contours = h[0]

print(len(contours))
coordinate_len_list = []
for i in range(0,len(contours)):
    #print(len(contours[i]))
    if len(contours[i]) > 100:
        coordinate_len_list.append(len(contours[i]))
print(sorted(coordinate_len_list)[-26:])
print(len(coordinate_len_list))
#print(len(contours[0]))
#print(contours[0][0][0])