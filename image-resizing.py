import cv2

img = cv2.imread('./images/extract.png')

# Using dsize
print(img.shape)   
out = cv2.resize(img, (600,600))
print(out.shape)

# Using fx and fy
out1 = cv2.resize(img, None, fx=2, fy=2)
print(out1.shape)

