import cv2
import torch
from PIL import Image
import numpy as np
import scipy.misc

def classify_corn(img1,img2):
    #count1 = 0
    #count2 = 0
    x1, y1 = (img1 < 120).nonzero()
    x2, y2 = (img1 > 100).nonzero()
    print(str(x1)+','+str(y1))
    print(str(x2)+','+str(y2))
    #print(len(x))
    #print(len(y))

    for i in range(0,len(x1)):
        img1[x1[i]][y1[i]] = 0
    for i in range(0,len(x2)):
        img2[x2[i]][y2[i]] = 0
    #img1 = img1[x, y]
    # for i in range(0,3999):
    #     for j in range(0,6015):
    #         #筛选出白色（好玉米）
    #         if img1[i][j] <= 120 and img1[i][j] >= 1:
    #             img1[i][j] = 0
    #             count1 = count1 + 1
    #             print(str(count1) +',',end="")
    #         #筛选出灰色（坏玉米）
    #         if img2[i][j] > 110:
    #             img2[i][j] = 0
    #             count2 = count2 + 1
    #             print(str(count2) +',',end="")
    return img1,img2


for i in range(38,48):
    #print(i)
    #转换成灰度图
    #image = Image.open('C:/Users/Adm/Desktop/corn/55small/55' + str(i) + '-1.jpg')
    #image = Image.open('C:/Users/Adm/Desktop/corn/55small/_DSC28' + str(i) + ' 拷贝.jpg')
    image = Image.open('C:/Users/Adm/Desktop/corn/1080/_DSC28' + str(i) + ' 拷贝.jpg')
    # #image = Image.open('C:/Users/Adm/Desktop/玉米/result1.jpg')

    image = image.convert('L') # convert image to black and white
    #image.save('C:/Users/Adm/Desktop/corn/gray_scale/_DSC28' + str(i) + '_gray_result.jpg')
    image.save('C:/Users/Adm/Desktop/corn/1080/gray/_DSC28' + str(i) + '_gray_result.jpg')

    #image1 = Image.open('C:/Users/Adm/Desktop/corn/gray_scale/_DSC28' + str(i) + '_gray_result.jpg')
    #image2 = Image.open('C:/Users/Adm/Desktop/corn/gray_scale/_DSC28' + str(i) + '_gray_result.jpg')
    image1 = Image.open('C:/Users/Adm/Desktop/corn/1080/gray/_DSC28' + str(i) + '_gray_result.jpg')
    image2 = Image.open('C:/Users/Adm/Desktop/corn/1080/gray/_DSC28' + str(i) + '_gray_result.jpg')
    corn_img1 = np.array(image1)
    corn_img2 = np.array(image2)



    # find good corn
    # def find_goodcorn(img):
    #     count = 0
    #     for i in range(0,3999):
    #         for j in range(0,6015):
    #             #print(img[i][j])
    #             if img[i][j] <= 150 and img[i][j] >= 1:
    #                 img[i][j] = 0
    #                 count = count + 1
    #                 print(str(count) +',',end="")
    #             print(str(img[i][j])+',',end="")
    #     return img


    #find bad corn
    # def find_badcorn(img):
    #     count = 0
    #     for i in range(0,3999):
    #         for j in range(0,6015):
    #             #print(img[i][j])
    #             if img[i][j] > 110:
    #                 img[i][j] = 0
    #                 count = count + 1
    #                 print(str(count) +',',end="")
    #     return img


    goodcorn_img, badcorn_img = classify_corn(corn_img1,corn_img2)

    image_array = np.array(goodcorn_img)
    image = Image.fromarray(image_array)
    image.save('C:/Users/Adm/Desktop/corn/1080/good/_DSC28' + str(i) + '_gray_result_good.jpg')

    image_array = np.array(badcorn_img)
    image = Image.fromarray(image_array)
    image.save('C:/Users/Adm/Desktop/corn/1080/bad/_DSC28' + str(i) + '_gray_result_bad.jpg')



# test
# image = Image.open('C:/Users/Adm/Desktop/corn/640/5501-640.jpg')
# image = image.convert('L') # convert image to black and white
# image.save('C:/Users/Adm/Desktop/corn/640/gray/5501-640_gray_result.jpg')
# image2 = Image.open('C:/Users/Adm/Desktop/corn/640/gray/5501-640_gray_result.jpg')
# corn_img2 = np.array(image2)

#print(classify_corn(corn_img2))
# badcorn_img = classify_corn(corn_img2)
# image_array = np.array(badcorn_img)
# print(image_array)
# image = Image.fromarray(badcorn_img)
# image.show()

#image.save("C:/Users/Adm/Desktop/corn/good_res.jpg")