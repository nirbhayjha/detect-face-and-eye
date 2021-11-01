import cv2
import numpy as np

def cross(x):
    pass

img= np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("colour picker")

s1= "0:OFF\n1:ON"
cv2.createTrackbar(s1, "colour picker", 0, 1, cross)

cv2.createTrackbar("R", "colour picker", 0, 255, cross)
cv2.createTrackbar("G", "colour picker", 0, 255, cross)
cv2.createTrackbar("B", "colour picker", 0, 255, cross)

while True:
    cv2.imshow("colour picker", img)
    k= cv2.waitKey(1)
    if k==ord("z") & 0xFF:
        break
    
    s= cv2.getTrackbarPos(s1, "colour picker") 
    r= cv2.getTrackbarPos("R", "colour picker") 
    g= cv2.getTrackbarPos("G", "colour picker") 
    b= cv2.getTrackbarPos("B", "colour picker") 
    
    if s==0:
        img[:]= 0
    else:
        img[:]= [r,g,b]


cv2.destroyAllWindows() 