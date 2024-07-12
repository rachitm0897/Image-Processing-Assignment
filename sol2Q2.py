import cv2 
import numpy as np 

# I have written a very huge code and its mostly hardcoding 

frame = np.zeros((300,500),dtype=np.uint8)
org11 = (2+41,30)
org12 = (2+41+82,30)
org13 = (2+41+82+82,30)

org21 = (43,90)
org22 = (2+41+82,90)
org23 = (2+41+82+82,90)

org31 = (43,90+60)
org32 = (2+41+82,90+60)
org33 = (2+41+82+82,90+60)

org41 = (43,90+120)
org42 = (2+41+82,90+120)
org43 = (2+41+82+82,90+120)

org51 = (43,90+120+60)
org52 = (2+41+82,90+120+60)
org53 = (2+41+82+82,90+120+60)

def one(frame,org):
    cv2.circle(frame,(org21[0]+org , org21[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org12[0]+org , org12[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org22[0]+org , org22[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org32[0]+org , org32[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org42[0]+org , org42[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org52[0]+org , org52[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org51[0]+org , org51[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)

def two(frame,org):
    cv2.circle(frame,(org11[0]+org,org11[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org12[0]+org , org12[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org13[0]+org , org13[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org23[0]+org , org23[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org31[0]+org , org31[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org32[0]+org , org32[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org33[0]+org , org33[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org41[0]+org , org43[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org51[0]+org , org51[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org52[0]+org , org52[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)

def three(frame,org):
    cv2.circle(frame,(org11[0]+org,org11[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org12[0]+org , org12[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org13[0]+org , org13[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org23[0]+org , org23[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org31[0]+org , org31[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org32[0]+org , org32[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org33[0]+org , org33[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org43[0]+org , org43[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org51[0]+org , org51[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org52[0]+org , org52[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)

def four(frame,org):
    cv2.circle(frame,(org11[0]+org,org11[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org13[0]+org , org13[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org21[0]+org , org21[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org23[0]+org , org23[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org31[0]+org , org31[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org33[0]+org , org33[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org32[0]+org , org32[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org43[0]+org , org43[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)

def five(frame,org):
    cv2.circle(frame,(org11[0]+org,org11[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org12[0]+org , org12[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org13[0]+org , org13[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org21[0]+org , org21[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org31[0]+org , org31[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org32[0]+org , org32[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org33[0]+org , org33[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org43[0]+org , org43[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org51[0]+org , org51[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org52[0]+org , org52[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)

def six(frame,org):
    cv2.circle(frame,(org11[0]+org,org11[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org12[0]+org , org12[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org13[0]+org , org13[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org21[0]+org , org21[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org31[0]+org , org31[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org32[0]+org , org32[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org33[0]+org , org33[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org43[0]+org , org43[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org51[0]+org , org51[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org52[0]+org , org52[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org41[0]+org , org41[1]),25,(255,255,255),-1)

def seven(frame,org):
    cv2.circle(frame,(org11[0]+org,org11[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org12[0]+org , org12[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org13[0]+org , org13[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org23[0]+org , org23[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org33[0]+org , org33[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org43[0]+org , org43[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)

def eight(frame,org):
    cv2.circle(frame,(org11[0]+org,org11[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org12[0]+org , org12[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org13[0]+org , org13[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org21[0]+org , org21[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org31[0]+org , org31[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org32[0]+org , org32[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org33[0]+org , org33[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org43[0]+org , org43[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org51[0]+org , org51[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org52[0]+org , org52[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org41[0]+org , org41[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org23[0]+org , org23[1]),25,(255,255,255),-1)

def nine(frame,org):
    cv2.circle(frame,(org11[0]+org,org11[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org13[0]+org , org13[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org21[0]+org , org21[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org23[0]+org , org23[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org31[0]+org , org31[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org33[0]+org , org33[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org32[0]+org , org32[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org43[0]+org , org43[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org12[0]+org , org12[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org51[0]+org , org51[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org52[0]+org , org52[1]),25,(255,255,255),-1)

def zero(frame,org):
    cv2.circle(frame,(org11[0]+org,org11[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org12[0]+org , org12[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org13[0]+org , org13[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org21[0]+org , org21[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org23[0]+org , org23[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org31[0]+org , org31[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org33[0]+org , org33[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org41[0]+org , org41[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org43[0]+org , org43[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org51[0]+org , org51[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org52[0]+org , org52[1]),25,(255,255,255),-1)
    cv2.circle(frame,(org53[0]+org , org53[1]),25,(255,255,255),-1)

number = int(input("Enter the Number: "))
d1 = number%10
number = number//10
d2 = number%10
count=1
for i in [d2,d1]:
    if i == 1:
        if count == 1:
            one(frame,0)
        else :
            one(frame,250)
    
    if i == 2:
        if count == 1:
            two(frame,0)
        else :
            two(frame,250)
    
    if i == 3:
        if count == 1:
            three(frame,0)
        else :
            three(frame,250)

    if i == 4:
        if count == 1:
            four(frame,0)
        else :
            four(frame,250)

    if i == 5:
        if count == 1:
            five(frame,0)
        else :
            five(frame,250)

    if i == 6:
        if count == 1:
            six(frame,0)
        else :
            six(frame,250)
    
    if i == 7:
        if count == 1:
            seven(frame,0)
        else :
            seven(frame,250)

    if i == 8:
        if count == 1:
            eight(frame,0)
        else :
            eight(frame,250)

    if i == 9:
        if count == 1:
            nine(frame,0)
        else :
            nine(frame,250)

    if i == 0:
        if count == 1:
            zero(frame,0)
        else :
            zero(frame,250)
    # break
    count+=1



cv2.imshow("Frame",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()