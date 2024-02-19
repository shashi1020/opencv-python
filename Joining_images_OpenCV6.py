import cv2
import numpy as np

img = cv2.imread("street.jpg")


imgHor = np.hstack((img,img))
'''images must have same number of channels'''
imgVer = np.vstack((img,img))

cv2.imshow("horizontal stack",imgHor)
cv2.imshow("vertical stack",imgVer)

cv2.waitKey(0)