import cv2

img=cv2.imread('face.png')
(h,w)=img.shape[:2]

center =(w/2,h/2)

angle90=90
angle180=180
angle270=270

scale=1.0
 #90 degree
M=cv2.getRotationMatrix2D(center,angle90,scale)
rotated90=cv2.warpAffine(img,M,(h,w))

 #180 degree
M=cv2.getRotationMatrix2D(center,angle180,scale)
rotated180=cv2.warpAffine(img,M,(w,h))

 #270 degree
M=cv2.getRotationMatrix2D(center,angle270,scale)
rotated270=cv2.warpAffine(img,M,(h,w))


#display images
cv2.imshow('Original Image',img)

cv2.imshow('Image rotated in 90 degree',rotated90)

cv2.imshow('Image rotated in 180 degree',rotated180)

cv2.imshow('Image rotated in 270 degree',rotated270)


