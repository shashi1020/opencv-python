import cv2
import numpy as np

path = "lamBo.jpg"

def empty(a):
    pass



cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",680,240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 47, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 199, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    #imgHSV = cv2.cvtcolor(img, cv2.COLOR_BGR2HSV)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    H_Min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    H_Max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    S_Min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    S_Max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    V_Min = cv2.getTrackbarPos("Value Min", "TrackBars")
    V_Max = cv2.getTrackbarPos("Value Max", "TrackBars")
    
    print(H_Min,H_Max,S_Min,S_Max,V_Min,V_Max)
    lower = np.array([H_Min,S_Min,V_Min])
    upper = np.array([H_Max,S_Max,V_Max])
    
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    
    
    cv2.imshow("original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("result",imgResult)
    cv2.waitKey(1)
    
    