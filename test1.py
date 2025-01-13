import cv2
import numpy as np

img_grey = cv2.imread("basketball.jpg",0)
img_color = cv2.imread("basketball.jpg",1)

#cv2.imshow("j",img_grey)
# Waits for a keystroke
#cv2.waitKey(0)  
cv2.imwrite("grey.jpg",img_grey)

# Destroys all the windows created
print("success")

new = cv2.resize(img_color, None, fx=2,fy=1, interpolation=cv2.INTER_NEAREST)
cv2.imwrite("400x400.jpg",new)
print(img_color[50][150])