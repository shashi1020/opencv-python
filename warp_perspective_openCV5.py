import cv2
import numpy as np

img = cv2.imread("card.png")
width,height = 344,220

pts1 = np.float32([[2932,834],[70,218],[448,1804],[1643,77]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Output image", imgOutput)

cv2.waitKey(0)

