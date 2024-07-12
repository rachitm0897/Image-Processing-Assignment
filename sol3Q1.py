import cv2
import numpy as np
import os

img_no = (input("Enter the Image No. :"))

img = cv2.imread("Image Processing/Assignment/Assignment_3_images/gutters"+img_no+".jpg")
img = cv2.resize(img,(700,500))
rgb_planes = cv2.split(img)
contrast=1.0
bright=0
result_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    result_planes.append(diff_img)
    # for i in plane:
    #     for j in i:
    #         j=j*contrast +bright
result = cv2.merge(result_planes)
imggray = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
adaptive_thresh = cv2.adaptiveThreshold(imggray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 8)
# blur = cv2.blur(adaptive_thresh,(1,1),)
# dilated= cv2.dilate(blur, (3,3))
# adaptive_thresh = cv2.cvtColor(new,cv2.COLOR_BGR2GRAY)

cv2.imshow('result', result)
cv2.imshow('thresh', adaptive_thresh)
# cv2.imshow("dilated",dilated)

cv2.waitKey(0)