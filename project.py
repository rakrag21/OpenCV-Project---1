import cv2
import numpy as np

vid = cv2.VideoCapture('video.mp4')
img = cv2.imread('pic.jpg')

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(img,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_g = np.array([32,94,132])
    u_g = np.array([179,255,255])

    mask = cv2.inRange(hsv,l_g,u_g)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    fsub = frame - res
    green_screen = np.where(fsub==0,image,fsub)
    cv2.imshow('Green Screen',green_screen)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()