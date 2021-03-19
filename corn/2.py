import cv2
import torch
from PIL import Image
import numpy as np
from skimage import io,data,color

#image = Image.open('C:/lab/玉米种子新数据集/标记55/_DSC2838 拷贝.jpg')
image = Image.open('C:/lab/玉米种子新数据集/标记55/_DSC2838 拷贝.jpg')
#image = Image.open('C:/Users/Adm/Desktop/玉米/result1.jpg')

# image = image.convert('1') # convert image to black and white
# image.save('C:/Users/Adm/Desktop/玉米/result2.jpg')

# image = Image.open('C:/Users/Adm/Desktop/玉米/result2.jpg')

#img=data.lena()
img_gray=color.rgb2gray(image)
#print(img_gray)
# rows,cols=img_gray.shape
# for i in range(rows):
#     for j in range(cols):
#         if (img_gray[i,j]<=0.5):
#             img_gray[i,j]=0
#         else:
#             img_gray[i,j]=1
# io.imshow(img_gray)