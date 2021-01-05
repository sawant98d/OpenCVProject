import cv2
# for reading images
"""
img = cv2.imread('resources/cr5.jpg')
cv2.imshow("Legend of foodboll",img)
cv2.waitKey(0)
"""

# for reading video
"""
cap = cv2.VideoCapture('resources/androidvid.mp4')
cnt = 1
while True:
    success, img = cap.read()
    cv2.imshow("Android"+str(cnt),img)
    if ord('q') == cv2.waitKey(1):
        break
    cnt+=1
"""
# for reading webcam

cap = cv2.VideoCapture(0) # it select default web camera from your laptop or pc
cap.set(3, 640)   # height of the frame
cap.set(4, 480)   # width of the frame
cap.set(10, 100)  # for setting the brightness
cnt = 1
while True:
    success, img = cap.read()
    cv2.imshow("Webcamera"+str(cnt),img)
    if ord('q') == cv2.waitKey(1):
        break
    #cnt+=1