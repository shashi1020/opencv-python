import cv2

cap = cv2.VideoCapture(0)
"Width"
cap.set(3, 640)
"height"
cap.set(4, 480)
"brightness"
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break