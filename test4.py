import numpy as np
import cv2
import time
import multiprocessing
from math import ceil, floor

from detect_circle import haar_circle_bl

print(1)
temp = cv2.imread("test.jpg", 0)
temp = cv2.resize(temp, None, fx=1, fy=1, interpolation=cv2.INTER_NEAREST)
og = cv2.imread("reduced.jpg")
og = temp
cv2.imwrite("reduced.jpg",og)
for i in range(5,250):
    
    mask = haar_circle_bl(i)/(i**2)*0.82
    end = cv2.filter2D(src=og,ddepth=-1, kernel=mask)

    max_index_flat = np.argmax(end)
    max_index = np.unravel_index(max_index_flat, end.shape)
    #print("Index of maximum value:", max_index)
    end[max_index[0]][max_index[1]] = 255
    cv2.imwrite(f"convolutions/{i}.jpg",end)
    
print("3")
print(np.sum(mask))
