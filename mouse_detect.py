import cv2
import numpy as np

m_cascade = cv2.CascadeClassifier('mouse_cascade.xml')

cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mouses = m_cascade.detectMultiScale(gray, 30,30)

    for (x,y,w,h) in mouses:
        cv2.rectangle(img ,(x,y), (x+w,y+h), (255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img , 'Mouse', (x-w, y-h), font, 0.5, (0,255,255), 2)

    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff

    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
