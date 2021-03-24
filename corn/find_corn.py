import cv2
import torch
from PIL import Image
import numpy as np
import scipy.misc
from PIL import Image 


# image = Image.open('C:/lab/玉米种子新数据集/标记55/_DSC2838 拷贝.jpg')
# #image = Image.open('C:/Users/Adm/Desktop/玉米/result1.jpg')

# image = image.convert('L') # convert image to black and white
# image.save('C:/Users/Adm/Desktop/玉米/result2.jpg')

image = Image.open('C:/Users/Adm/Desktop/玉米/result2.jpg')
corn_img = np.array(image)
# for i in img[200]:
#     print(str(i)+',',end="")
#print(img)
#img[0][0] = 0

# print(img[3999])
# for i in img[2000]:
#     if i < 200 and i > 5:
#         print(i)


# find good corn
def find_goodcorn(img):
    count = 0
    for i in range(0,3999):
        for j in range(0,6015):
            #print(img[i][j])
            if img[i][j] <= 150 and img[i][j] >= 1:
                img[i][j] = 0
                count = count + 1
                print(str(count) +',',end="")
            print(str(img[i][j])+',',end="")
    return img


#find bad corn
def find_badcorn(img):
    count = 0
    for i in range(0,3999):
        for j in range(0,6015):
            #print(img[i][j])
            if img[i][j] > 110:
                img[i][j] = 0
                count = count + 1
                print(str(count) +',',end="")
    return img


# image_array = np.array(img)
# scipy.misc.imsave('C:/Users/Adm/Desktop/玉米/good_res.jpg', image_array)

badcorn_img = find_badcorn(corn_img)
image_array = np.array(badcorn_img)
scipy.misc.imsave('C:/Users/Adm/Desktop/玉米/bad_res2.jpg', image_array)

# image = Image.fromarray(img)
# image.show()
# image.save("C:/Users/Adm/Desktop/玉米/good_res.jpg")


#print(len(img[:][3000]))

# RGB = []
# for j in range(0,6016):
#     for i in range(0,4000):
#         print(img[i][j][0])
        #res = int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2])
        #if(res<700 and res > 5):
            #img[i][j] = [0,0,0]
        #RGB.append(res)
        #print(img[i][3000][2])

# im = Image.fromarray(img)
# im.save("good_res.jpeg")
# print(RGB)
    