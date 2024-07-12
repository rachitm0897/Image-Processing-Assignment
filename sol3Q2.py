import cv2
import numpy as np
# val=0
# sat=0
# Min=0
# threshH=0
# threshL=0

# def Val(value):
#     global val
#     val = value
# def Sat(value):
#     global sat
#     sat= value
# def Track(value):
#     global Min
#     Min = value
# def Minthresh(value):
#     global threshH
#     threshH = value
# def Maxthresh(value):
#     global threshL
#     threshL = value

# img_no = (input("Enter the Image No. :"))

# frame= cv2.imread("Image Processing/Assignment/Assignment_3_images/cctv"+img_no+".jpg")
# frame = cv2.imread(r"C:\Users\91987\OneDrive - IIT Kanpur\Desktop\Eclub\Images\cctv3.JPG")
# frame = cv2.imread(r"C:\Users\91987\Downloads\WhatsApp Image 2023-07-18 at 20.36.58.jpg")
frame = cv2.imread(r"C:\Users\91987\Downloads\WhatsApp Image 2023-10-19 at 03.28.14_f800adae.jpg")
frame = cv2.resize(frame,(500,700))
#for setting the best values possible

# cv2.namedWindow("Track")

# cv2.createTrackbar("Val","Track",0,255,Val)
# cv2.createTrackbar("Sat","Track",0,255,Sat)
# cv2.createTrackbar("Min","Track",0,255,Track)
# cv2.createTrackbar("threshMin","Track",0,255,Minthresh)
# cv2.createTrackbar("threshMax","Track",0,255,Maxthresh)

frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

# I was getting 4,15 as the best set of values 
new = np.zeros_like(frame)
contrast=100
bright=60

val=34
    # i,j,c = 0,100,1
    # print("frame",frame[i,j,c])
    # print(np.clip(contrast*frame[i,j,c]+bright,0,255))

for i in range(len(frame)):
    for j in range(len(frame[i])):
        if frameHSV[i][j][2]+val<255:
            frameHSV[i][j][2] = frameHSV[i][j][2]+val
        # for c in range(len(frame[i][j])):
        #     new[i,j,c] = np.clip(contrast*frame[i,j,c]+bright,0,255) #Convention 
# print(bright,contrast)
# framenormal = cv2.cvtColor(new,cv2.COLOR_HSV2BGR)
framehhh = cv2.cvtColor(frameHSV,cv2.COLOR_HSV2BGR)
# for i in range(len(frame)):
#     for j in range(len(frame[i])):
#         for c in range(len(frame[i][j])):
#             if contrast*frame[i,j,c]+bright<255:
#                 new[i,j,c] = contrast*frame[i,j,c]+bright
# blur = cv2.GaussianBlur(new,(3,3),0)
# dilate = cv2.dilate(blur,(7,7))
    
# framenormal = cv2.cvtColor(frameHSV,cv2.COLOR_HSV2BGR)
# cv2.imshow("Frame",frameHSV)
  
# adaptive_thresh = cv2.adaptiveThreshold(framenormal,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 3) 
# cv2.imshow("Frameenhanced",new)
cv2.imshow("Before",frame)
cv2.imshow("Frameinitial",framehhh)
# cv2.imshow("Frame",dilate)
# break
cv2.waitKey(0) 
cv2.destroyAllWindows()

# import cv2
# import numpy as np

# img = cv2.imread(r'C:\Users\91987\Documents\python\Image Processing\Assignment\Assignment_3_images\cctv1.JPG', 1)
# # converting to LAB color space
# img = cv2.resize(img,(700,500))
# lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# l_channel, a, b = cv2.split(lab)

# # Applying CLAHE to L-channel
# clahe = cv2.createCLAHE(clipLimit=15, tileGridSize=(3,3))
# cl = clahe.apply(l_channel)

# # merge the CLAHE enhanced L-channel with the a and b channel
# limg = cv2.merge((cl,a,b))

# # Converting image from LAB Color model to BGR color spcae
# enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

# # Stacking the original image with the enhanced image
# result = np.hstack((img, enhanced_img))
# cv2.imshow('Result', result)
# cv2.waitKey(0)
