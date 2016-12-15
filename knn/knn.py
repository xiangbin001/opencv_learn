# coding=utf-8
import numpy as np
import cv2
# from matplotlib import pyplot as plt

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Now we split the image to 5000 cells, each 20x20 size
# 水平切50刀，竖直方向切100刀
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
# 图形矩阵
# print cells[49][99]; #像素点
# print cells[0][0].shape (20,20) pixel
# print type(cells)  #list
# print type(cells[49][99])

# cells类似于
# test = np.array([[1,2,3,4,5,6,3,10,255,233,255,33,0],[1,2,3,4,5,6,3,10,255,233,255,33,0],[6,5,4,3,2,1,3,10,255,233,255,33,0],[9,8,7,6,5,4,3,10,255,33,0,0,0]])

# Make it into a Numpy array. It size will be (50,100,20,20)
x = np.array(cells)
# cells 结构本身就是这样的打印相等为
# print x == cells,x is cells

# Now we prepare train_data and test_data.
# s = x[:,:2].reshape(-1,400).astype(np.float32)
# print s[10][1]
# 矩阵重排
train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400) # 20*20 == 400 ,所以400一行，2500行
#400个一行，应该有（25/4）+1行，最后一行 没满
test = x[:,98:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)
# s = x[:,:50] #左右取 截取左边0-49列，总共50 * 5 *100 = 2500个
# .reshape 矩阵转换
# test[0][0] = 1
# print test[0]

# Create labels for train and test data
k = np.arange(10)
# nump.array([0,1,2,3,4,5,6,7,8,9])
# train_labels = np.repeat(k,250)[:,np.newaxis]
train_labels = np.repeat(k,250)[:,np.newaxis]
# test_labels = train_labels.copy()
# test_labels = np.repeat(k,250)[:,np.newaxis]


# # Initiate kNN, train the data, then test it with test data for k=1
knn = cv2.KNearest()
knn.train(train,train_labels)
ret,result,neighbours,dist = knn.find_nearest(test,k=1)

print result


# # # Now we check the accuracy of classification
# # # For that, compare the result with test_labels and check which are wrong
# matches = result==test_labels
# # # # print type(matches) 
# # # # 矩阵之间判断你相等会根据一个一个的矩阵内的值来判断
# # # # 结果类似于[[True][True][True][True],[True][True][True][True],[True][True][True][True],[True][True][True][True]]

# correct = np.count_nonzero(matches)
# accuracy = correct*100.0/result.size
# print accuracy

# # save the data
# np.savez('knn_data.npz',train=train, train_labels=train_labels)

# # Now load the data
# with np.load('knn_data.npz') as data:
#     print data.files
#     train = data['train']
#     train_labels = data['train_labels']