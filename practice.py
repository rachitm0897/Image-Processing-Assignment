from PIL import Image, ImageEnhance
import cv2
#read the image
# im = Image.open(r"C:\Users\91987\Documents\python\Image Processing\Assignment\Assignment_3_images\cctv4.JPG")
# factor=1
# #image brightness enhancer
# enhancer = ImageEnhance.Brightness(im)
# def Factor(value):
#     global factor
#     factor=value
# cv2.namedWindow("Track")
# cv2.createTrackbar("Factor","Track",0,10,Factor)

# while True:
#     im_output = enhancer.enhance(factor)
#     im_output.save(r"C:\Users\91987\Documents\python\Image Processing\Assignment\Assignment_3_images\brightened-image.jpg")
#     cam=cv2.VideoCapture(r"C:\Users\91987\Documents\python\Image Processing\Assignment\Assignment_3_images\brightened-image.jpg")
#     ignore,frame = cam.read()
#     cv2.imshow("Frame",frame)
#     if cv2.waitKey(1) & 0xff==ord('q'):
#         break


# import cv2
# import numpy as np 
# img = cv2.imread(r'C:\Users\91987\Documents\python\Image Processing\Assignment\Assignment_3_images\cctv2.JPG')
# new =  np.zeros_like(img)

# contrast = 2
# bright = 5

# for i in range(len(img)):
#     for j in range(len(img[i])):
#         for c in range(len(img[i][j])):
#             new[i,j,c] = np.clip(contrast*img[i,j,c]+bright,0,255)                  
            

# cv2.imshow("img",img)
# cv2.imshow("img",new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np 
from math import *
# C:\Users\91987\Documents\python\Resources\Photos\cat.jpg
# C:\Users\91987\Documents\python\Image Processing\Assignment\Assignment_3_images\cctv2.JPG
img = cv2.imread(r'C:\Users\91987\Documents\python\Image Processing\Assignment\Assignment_3_images\cctv1.JPG')
new =  np.zeros_like(img)

contrast = 2
bright = 5
l=200
c = 250 / np.log(1 + np.max(img))
new = c * (np.log(img + 1))
new = np.array(new, dtype = np.uint8) #log
const=2
y=0.5
# for i in range(len(img)):
#     for j in range(len(img[i])):
#         for c in range(len(img[i][j])):
#             # print()
#             # new[i,j,c] = 255-img[i][j][c] negative  
#             # new[i,j,c] = 255*((img[i][j][c]/255)**y )  #power transformations
#             # new[i,j] = 255*(img[i,j]-np.min(img))/(np.max(img)-np.min(img))
                 
            

cv2.imshow("img",img)
cv2.imshow("img1",new)
cv2.waitKey(0)
cv2.destroyAllWindows()