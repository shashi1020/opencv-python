import cv2
import numpy as np
###########################################
widthImg = 640
heightImg = 640
###########################################
cap = cv2.VideoCapture(0)



def preprocessing(img):
    imgGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBLUR = cv2.GaussianBlur(imgGRAY, (5, 5), 1)
    imgCANNY = cv2.Canny(imgBLUR, 200, 200)
    kernel = np.ones((5,5))
    imgDIAL = cv2.dilate(imgCANNY,kernel, iterations=2)
    imgTHRES = cv2.erode(imgDIAL, kernel, iterations=1)
    return imgTHRES

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>5000:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt, True)
            print("arcLength: "+ str(peri))
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    return biggest
            
           
            

while True:
    success, img = cap.read()
    cv2.resize(img,(widthImg,heightImg))
    imgContour = img.copy()
    imgTHRES = preprocessing(img)
    biggest =  getContours(imgTHRES)
    cv2.imshow("webcam", imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break