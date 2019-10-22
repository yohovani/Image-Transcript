import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('/home/yohovani/Pictures/TT/DCIM/100CANON/IMG_1404.JPG',0)
img = cv.medianBlur(img,5)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
cv.imshow("Original", img)
cv.imshow("Global Thresholding (v = 127)", th1)
cv.imshow("Adaptive Mean Thresholding", th2)
cv.imshow("Adaptive Gaussian Thresholding", th3)
cv.waitKey(0)