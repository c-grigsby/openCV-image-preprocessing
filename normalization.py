import cv2
import numpy as np


# Divide by max
def divide_by_max(img):
    return img/255
    
# Min-Max Scaling  
def min_max(img):
    img_min = np.min(img)
    img_max = np.max(img)
    return (img - img_min)/(img_max - img_min)
    
# Standardization
def standardize(img):
    mu = img.mean()
    std = img.std()
    return (img - mu)/std
