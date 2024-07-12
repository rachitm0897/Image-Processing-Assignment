import numpy as np 
import cv2
size = 1
areamin =1
threshmin = 1
threshmax= 1
def Size(val):
    global size 
    size =val

def Area(val):
    global areamin
    areamin = val

def ThreshMin(val):
    global threshmin
    threshmin=val

def ThreshMax(val):
    global threshmax
    threshmax = val


ker = (size,size)
name = 'My Frame'
cv2.namedWindow(name)

# cv2.createTrackbar('Ker Size',name,1,13,Size)
cv2.createTrackbar('Area',name,1,10000,Area)

cv2.createTrackbar('Thresh Min',name,1,255,ThreshMin)
cv2.createTrackbar('Thresh Max',name,1,255,ThreshMax)


while True:
    cam = cv2.VideoCapture(r'C:\Users\91987\Documents\python\Image Processing\Assignment\jigsaw.jpg')
    ignore, frame = cam.read()

    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # blur = cv2.GaussianBlur(gray,ker,0)
    blur = cv2.medianBlur(gray,size)
    # blur = cv2.blur(gray,ker)
    # blur = cv2.bilateralFilter(gray,10,35,25)

    ret,thresh = cv2.threshold(blur,threshmin,threshmax,cv2.THRESH_BINARY)

    contours,junk=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    for contour in contours:
        area=cv2.contourArea(contour)
        if area>=areamin:
            #cv2.drawContours(frame,[contour],0,(255,0,0),3)
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    
    cv2.imshow(name,frame)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
