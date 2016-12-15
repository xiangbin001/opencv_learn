# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

test = cv2.imread('test.png')
test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

test = test.reshape(-1,400).astype(np.float32)

x = np.array(cells)

# 全部作为训练数据，矩阵重排然后位数浮点
# 5000行，400像素一组
train = x[:,0:100].reshape(-1,400).astype(np.float32) 

k = np.arange(10)
train_labels = np.repeat(k,500)[:,np.newaxis]

knn = cv2.KNearest()
knn.train(train,train_labels)

ret,result,neighbours,dist = knn.find_nearest(test,k=1)

print result