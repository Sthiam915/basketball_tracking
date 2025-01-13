import cv2
import numpy as np

def gaussian_kernel(size, sigma):
    kernel = np.fromfunction(lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size//2))**2 + (y-(size//2))**2)/(2*sigma**2)), (size, size))
    kernel /= np.sum(kernel)
    return kernel

img = cv2.imread("ball2.jpg", 0)
cv2.imwrite("original.jpg",img)

gauss1 = img.ravel()
gauss1 = np.convolve(gaussian_kernel(6,1.5).ravel(), gauss1)
gauss1 = gauss1[:-35]

gauss2 = img.ravel()
gauss2 = np.convolve(gaussian_kernel(3,1.5).ravel(), gauss2)
gauss2 = gauss2[:-8]

gaussdiff = np.subtract(gauss1,gauss2)
gaussdiff = np.reshape(gaussdiff, img.shape)
cv2.imwrite("ball.jpg", gaussdiff)