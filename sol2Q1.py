import cv2 
import numpy as np 

cam = cv2.VideoCapture(r'C:\Users\91987\Documents\python\Image Processing\Assignment\jigsaw.jpg')
ignore,frame = cam.read()
print(frame.shape)
# making the copy to not mess with the original 
img = frame.copy()
cv2.imshow("My Frame 1 ",frame)
# deciding Region of Intrests
roi1 = img[:200,:190]
roi2 = img[200:400,:190]
roi3 = img[150:330,515:700 ]
roi4 = img[370:421,370:797]

# changing them to the original places using simple traversing 
# and using the flip question
frame[:200,:190]=cv2.flip(roi2,0)
frame[195:395,:190]=roi1
frame[150:330,515:700]=cv2.flip(roi3,1)
frame[370:421,370:797] = cv2.flip(roi4,0)


# cv2.imshow("ROI1",roi1)
# cv2.imshow("ROI2",roi2)
# cv2.imshow("ROI3",roi3)
# cv2.imshow("ROI4",roi4)
cv2.imshow("My frame",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()