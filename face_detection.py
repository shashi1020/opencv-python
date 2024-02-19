#we are going to use method peoposed by viola and jones
import cv2

faceCascade = cv2.CascadeClassifier("path to cascade file")
img = cv2.imread("shashi.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0), 2)



