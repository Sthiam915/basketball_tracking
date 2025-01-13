import cv2

layup = cv2.VideoCapture("layup.mp4")

if layup.isOpened():
    print("opened video!")
    
    print(layup.get())
else:
    print("failed to open video!")
    