#coding=utf-8
import cv2
import numpy as np
img = cv2.imread('123.jpg',0)
# 如果出错不返回任何error
# print img

# 直接打开图片
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 先打开一个窗口，然后在窗口中放入图片
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 应该是保存，但是会出错不知道原因
# cv2.imwrite('messigray.png', img)

# 按 ESC 退出， 按S保存退出
# cv2.imshow('imaged',img)
# k = cv2.waitKey(0) & 0xFF
# if k == 27:
# 	cv2.destroyAllWindows()
# elif k == ord('s'):
# 	cv2.imwrite('messigray.png',img)
# 	cv2.destroyAllWindows()

