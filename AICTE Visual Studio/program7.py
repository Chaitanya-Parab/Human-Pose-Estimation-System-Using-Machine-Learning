import numpy as np
import cv2
font=cv2.FONT_HERSHEY_SIMPLEX

img=cv2.imread("face.png",1)
cv2.putText(img,'Chaitanya',(20,45),font,2,(0,200,140),5)

cv2.imshow("image",img)
cv2.waitKey(0)
