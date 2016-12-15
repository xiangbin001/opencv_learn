import numpy as np
import cv2

cap = cv2.VideoCapture('test.mp4')
print cap.isOpened()
# cap = cap.open('C:/var/learn/python/gui_feature/videos/test.mp4')
# while (cap.isOpened()):
# while (True):
# 	ret, frame = cap.read()
# 	print ret, frame
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# cv2.imshow('frame', gray)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	# 	break

# # when everythin done ,release the capture
# cap.release()
# cv2.destroyAllWindows()