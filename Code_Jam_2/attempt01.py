from cv2 import cv2
import numpy as np
cap = cv2.VideoCapture('sentry3.mkv')
def func(x):
    if cv2.contourArea(x) < 100 and cv2.contourArea(x) > 30:
        return cv2.contourArea(x)
    return 0
while True:
    ret1,frame = cap.read()
    if ret1 == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        l_b = np.array([0,0,156])
        u_b = np.array([255,20,178])
        mask = cv2.inRange(hsv, l_b, u_b) #mask
        res = cv2.bitwise_and(frame,frame,mask=mask)
        ret2, thresh = cv2.threshold(frame,127,255,cv2.THRESH_BINARY_INV)
        edges = cv2.Canny(res,170,200)
        contours,heirarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame,contours,-1,(0,255,0),2)
        cnt = sorted(contours, key=lambda x: cv2.contourArea(x),reverse=True)[0:2]
        try:
            for c in (cnt):
                (x,y,w,h) = cv2.boundingRect(c)
                cv2.rectangle(frame,(x-10,y+10),(x+w+10,y+h-10),(0,255,0),2)
                #cv2.putText(frame, 'Robo', (x, y-110), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        except:
            pass
        cv2.imshow('frame',frame)
        cv2.imshow('edges',edges)
    else :
        pass
    if cv2.waitKey(42) == 27: #fps=24;(1/fps)*1000=41.67
        cv2.destroyAllWindows()
        break