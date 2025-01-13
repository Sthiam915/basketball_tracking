import numpy as np
import cv2
import time
import multiprocessing
from math import ceil, floor

def haar_circle_bl(size):
    if size < 3:
        raise Exception("must be size 3 or greater")
    else:
        
        haar = np.ones((size, size))
        radius = size // 4
        center = size // 2
        for i in range(size):
            for j in range(size):
                if ((i-center) ** 2 + (j-center) ** 2) ** 0.5 <= floor(center * 0.789):
                    haar[i][j] = -1
        return haar

def mask(image_section, haar_mask):
    
    if haar_mask.shape != image_section.shape:
        raise Exception(f"Shapes must match => shape of mask is {haar_mask.shape}, but shape of section is {image_section.shape}")

    return np.sum(image_section * haar_mask)

def slide(image, haar_mask, size):
    max_strength = (0,0,0,0)
    rows, cols = image.shape
    for i in range(rows - size + 1):
        
        for j in range(cols - size + 1):
            
            image_section = image[i:i + size, j:j + size]
            strength = abs(mask(image_section, haar_mask)) / (size**2)
            if strength > max_strength[0]:
                max_strength = (strength, i, j, size)
    print(f"slid, size is {size}")
    return max_strength

def final(size):
    haar_mask = haar_circle_bl(size)
   
    return slide(img1, haar_mask, size)

if __name__ == "__main__":
    image_name = input("which image should be checked? ")
    a,haar_ex = cv2.threshold(haar_circle_bl(100),0,255,cv2.THRESH_BINARY)
    cv2.imwrite("haar.jpg", haar_ex)
    
    strengths = []
    img1 = cv2.imread(image_name, 0)
    img1 = cv2.resize(img1, None, fx=(200/img1.shape[0]), fy=(200/img1.shape[0]), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("drawn.jpg", img1)
    time1 = time.time()
    print("beginning")
    with multiprocessing.Pool() as pool:
        strengths = pool.map(final, range(50, 220))


  
    print(f"{floor(time.time() - time1)} seconds elapsed")
    print(img1.shape)
    
    strengths = sorted(strengths)
    a = strengths[-1]
    print(a)
    
    
    processed = cv2.circle(img1, (a[2] + a[3]//2, a[1] + a[3]//2), floor((a[3]//2) * 0.798), (255, 0, 0), 1)
    processed = cv2.rectangle(processed, (a[2], a[1]), (a[2] + a[3], a[1] + a[3]), (255, 0, 0))
 
    cv2.imwrite("drawn.jpg", processed)
    
   
    
    
