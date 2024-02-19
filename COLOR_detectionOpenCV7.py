import cv2
import numpy as np

def empty(a):
    pass

path = "lambo.jpg"

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("sat Min", "TrackBars", 47, 255, empty)
cv2.createTrackbar("sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("value Min", "TrackBars", 119, 255, empty)
cv2.createTrackbar("value Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    H_Min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    H_Max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    S_Min = cv2.getTrackbarPos("sat Min", "TrackBars")
    S_Max = cv2.getTrackbarPos("sat Max", "TrackBars")
    V_Min = cv2.getTrackbarPos("value Min", "TrackBars")
    V_Max = cv2.getTrackbarPos("value Max", "TrackBars")
    #value - brightness

    print(H_Min,H_Max,S_Min,S_Max,V_Min,V_Max)
    lower = np.array([H_Min,S_Min,V_Min])
    upper = np.array([H_Max,S_Max,V_Max])

    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow("original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("result",imgResult)
    cv2.waitKey(1)





