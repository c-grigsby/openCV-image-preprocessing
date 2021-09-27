import cv2
img = cv2.imread('./images/rotate.jpg')

cv2.imshow("img", img)
cv2.waitKey(0)

# Detect the box
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=cv2.contourArea, reverse=True)
max_cnt = contours[0]


# Find the skew angle
angle = cv2.minAreaRect(max_cnt)[-1]
if angle < -45:
    angle = 90 + angle
    
print(angle)


# Re-rotate the image
height, width, _ = img.shape
center = (width//2, height//2)

M = cv2.getRotationMatrix2D(center, angle, 1)
dst = cv2.warpAffine(img, M, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

# Display the image
cv2.imshow("out", dst)
cv2.waitKey(0)