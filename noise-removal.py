import cv2

img = cv2.imread('./images/salt-and-pepper.png')

cv2.imshow('img', img)
cv2.waitKey(0)

out = cv2.medianBlur(img, 5)
cv2.imshow('img', img)
cv2.imshow('out', out)
cv2.waitKey(0)
