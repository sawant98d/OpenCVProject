import cv2
import numpy as np

img = cv2.imread('resources/cr5.jpg')
kernel = np.ones((5,5), np.uint8)

height, width, channel = img.shape
print(height, width, channel)

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)              # converting img to grayscale image
blurImg = cv2.GaussianBlur(grayImg, (7,7),0)                 # converting img to blur image
cannyImg = cv2.Canny(img, 150, 200)                          # converting img to canny image
dialationImg = cv2.dilate(cannyImg, kernel, iterations=1)    # Dialation increases the width of the image

cv2.imshow("Gray Image", grayImg)                            # showing gray image
cv2.imshow("Blur Image", blurImg)                            # showing Blur image
cv2.imshow("Canny Image", cannyImg)                          # showing canny image
cv2.imshow("Dialation Image", dialationImg)                  # showing dialated image

cv2.waitKey(0)