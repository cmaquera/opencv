import numpy as np
import cv2

#load an color image in graysale
img = cv2.imread('messi5.jpg', 0)

#diplay the image
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


