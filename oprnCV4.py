" SHAPES and TEXTS "

import cv2
import numpy as np

img = np.zeros((512,512,3))
print(img.shape)

"coloring image"
img[0:100,200:300] = 255,0,255
"img[height,width] = color"

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
'''cv2.line(img,(starting point),(ending point),(RGB color),thickness) '''

cv2.rectangle(img,(156,356),(356,156),(0,0,255),3)
'''cv2.rectangle(img,(starting point),(ending point),(RGB color),thickness) '''

cv2.circle(img,(256,256),100,(255,255,0),5)
'''cv2.circle(img,(centre point),radius,(RGB color),thickness) '''


"HOW TO PUT TEXT ON IMAGES"
cv2.putText(img," OPENCV ",(300,100),cv2.FONT_HERSHEY_DUPLEX,1,(0,150,0),3)

'''cv2.putText(img," OPENCV ",(origin),cv2.FONT_HERSHEY_SIMPLEX,scale,(color),thickness)'''




cv2.imshow("Image",img)
cv2.waitKey(0)