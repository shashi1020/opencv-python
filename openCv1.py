"opencv functions"
import cv2
import numpy as np

img = cv2.imread("street.jpg")
kernel = np.ones((5,5),np.uint8)
'''kernel = np.ones((5, 5), np.uint8): This line creates a NumPy array named kernel, which is a 5x5 matrix filled with ones and of data type np.uint8. This is a common operation in image processing used for tasks like morphological operations, filtering, and convolution.'''


imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
'''cv2.COLOR_BGR2GRAY - converts colored image to gray color'''

imgBLUR = cv2.GaussianBlur(imgGRAY,(3,7),0)
'''This line of code applies a Gaussian blur to the grayscale image "imgGRAY" using a kernel size of (3,7) and a standard deviation of 0 '''

imgCanny = cv2.Canny(imgBLUR,150,200)
'''The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images'''

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
'''used is increase the thickness of image
n OpenCV Python, dilation is a morphological operation that is used to gradually enlarge (or 'dilate') the white regions (or objects) of an image while shrinking the black (or background) areas.

Here are a few reasons why we use image dilation:

Remove small black spots or noise: Image dilations can fill small holes caused by white noise on black objects, thus could be used to clean the image.

Join connected components: Dilations can connect nearby regions of an object. For example, in text analysis, if you have characters that are very close together, dilation could join them together into one object.

Enhance white area: If certain features of the object that are pale and not clearly visible, dilation can be used to enhance those areas'''

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
"Boundary Extraction: Erosion operation could also help to find the boundary of an object."

'''cv2.imshow("Gray image",imgGRAY)
cv2.imshow("Blur image",imgBLUR)'''
cv2.imshow("Canny image",imgCanny)
cv2.imshow("diation image",imgDialation)
cv2.imshow("eroded image",imgEroded)
cv2.waitKey(0)