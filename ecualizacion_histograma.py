import cv2
import numpy

img = cv2.imread('/home/yohovani/Pictures/TT/DCIM/IMG_1382.jpg', cv2.IMREAD_GRAYSCALE)

img = cv2.equalizeHist(img)
cv2.imwrite('result.jpg', img)

gray = cv2.imread('/home/yohovani/Pictures/TT/DCIM/IMG_1382.jpg', cv2.IMREAD_GRAYSCALE)  #pass 0 to convert into gray level
cv2.imshow('Escala de grises', gray)

#
_, dst1 = cv2.threshold(gray, 96, 255, cv2.THRESH_BINARY)
cv2.imshow("Fijo", dst1)
cv2.imwrite('./Otsu/thresholdEcualizado1382.jpg', dst1)
##
gray = cv2.medianBlur(gray, 5)
dst2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 6)
cv2.imshow('win1', dst2)
cv2.imwrite('./Otsu/adaptiveThresholdEcualizado1382.jpg', dst2)
cv2.waitKey(0)

