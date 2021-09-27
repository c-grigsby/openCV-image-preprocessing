import cv2

img = cv2.imread('./images/extract.png')

cv2.imshow('img', img)
cv2.waitKey(0)

# Convert to greyscale
out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('out', out)
cv2.waitKey(0)

