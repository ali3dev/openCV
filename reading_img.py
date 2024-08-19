# Reading an Image

import cv2
import numpy as np
import os

image = cv2.imread('ali.png')
h , w = image.shape[:2]
print(f'Height ${h} and Width ${w}')



(B, G, R) = image[100, 100]
print("R = {}, G = {}, B = {}".format(R, G, B))
B = image[100, 100, 0]
print("B = {}".format(B))

resize = cv2.resize(image,(300, 300))
h = np.hstack((resize, resize,resize))
v = np.vstack((h,h))

cv2.imshow('ali',v) 

roi = image[100 : 500, 200 : 700]
cv2.imshow("ROI", roi)


# list_name = os.listdir(r"D:\\openCV")
# list_name
# for name in list_name:
#     path = 'D:\\openCV'
#     img_name = path + '\\' + name 
#     img = cv2.imread(img_name)
#     img = cv2.resize(img,(500,600))
#     cv2.imshow("ALi", img)



cv2.waitKey(0)
cv2.destroyAllWindows()