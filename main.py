import cv2

img = cv2.imread("lambo.jpg")

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshoe("hsv",imgHSV)
cv2.waitKey(0)

# mycolors is a list of colors that we want to detect
myColors = [
            [116, 70, 122, 179, 176, 255],
            [5, 107, 0, 19, 255, 255],
            [71, 104, 133, 160, 171, 255]
             ]