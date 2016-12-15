# 二值化
# coding=utf-8
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lianzi.jpg')


image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  
cv2.threshold(image, 140, 255, 0, image)  
  
cv2.namedWindow("Image")  
cv2.imshow("Image", image)  
cv2.waitKey(0)  

# dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

# cv2.imwrite('new_lianzi.jpg',dst)

# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
# plt.show()