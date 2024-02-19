"how to resize and crop images"
import cv2
import numpy as np

img = cv2.imread("street.jpg")
print(img.shape)

''' how to resize an image '''
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

"how to crop image"
imgCropped = img[0:200,200:500]

cv2.imshow("cropped image",imgCropped)
cv2.imshow("image",img)
cv2.imshow("resized image",imgResize)

cv2.waitKey(0)