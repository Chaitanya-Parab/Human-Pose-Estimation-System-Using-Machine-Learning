import numpy as np
import cv2
img =cv2.imread('gan1.png',1)

cv2.circle(img,(80,80),55,(0,255,0),-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img=cv2.imread(r"face.png",1)
cv2.rectangle(img,(15,25),(200,150),(0,255,255),5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
