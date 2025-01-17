import cv2

img=cv2.imread('gan1.png',0)
print(img)
status=cv2.imwrite('ganapathy.png',img)
print("Image written to file-system : ",status)