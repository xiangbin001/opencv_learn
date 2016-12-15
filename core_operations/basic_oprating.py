# Basic Operations on Images
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#exercises

# some oprating like 
# img.item(10,10,2)
# img.itemset( (10,10,2), 100)
# img.shape
# img.size
# img.dtype
# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))
import cv2


img = cv2.imread('123.jpg')
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
# cv2.imwrite('new.jpg',img)