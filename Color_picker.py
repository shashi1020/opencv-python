import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 360)
cap.set(4, 340)
cap.set(10, 150)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 460, 240)
cv2.createTrackbar("Hue Min", "HSV", 0, 179, empty)
cv2.createTrackbar("Sat Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Value Min","HSV", 0, 255, empty)
cv2.createTrackbar("Hue Max","HSV", 179, 179, empty)
cv2.createTrackbar("Sat Max","HSV",255, 255, empty)
cv2.createTrackbar("Value Max","HSV", 255, 255,empty)

while True:
    ret, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_Min = cv2.getTrackbarPos("Hue Min", "HSV")
    h_Max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_Min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_Max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_Min = cv2.getTrackbarPos("Value Min", "HSV")
    v_Max = cv2.getTrackbarPos("Value Max", "HSV")

    print(h_Min)
    
    lower = np.array([h_Min,s_Min,v_Min])
    upper = np.array([h_Max,s_Max,v_Max])
    
    mask = cv2.inRange(imgHSV, lower, upper)
    print(mask)
    
    
    result = cv2.bitwise_and(img, img, mask = mask)
    
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    Hstack = np.hstack([img,mask,result])
    cv2.imshow("stack",Hstack)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()