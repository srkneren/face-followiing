import cv2
import numpy as np
import time
import serial


serx = serial.Serial("COM12",115200)
sery = serial.Serial("COM10",115200)
def dondurx(derece):
    
    serx.write(chr(derece).encode())

def dondury(derece):
    
    sery.write(chr(derece).encode())
    
def ayarla(kare,yuzde = 75):
    uzunluk = int(kare.shape[0] * yuzde/100)
    genislik = int(kare.shape[1] * yuzde/100)
    boyut = (uzunluk,int(genislik/2))

    return cv2.resize(kare,boyut,interpolation= cv2.INTER_AREA)
   
    
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('recognizer/trainningData.yml')
id=0

font=cv2.FONT_HERSHEY_COMPLEX
xkor = 0
while(True):
    ret,img=cam.read()
    
    
    cv2.pyrDown(img)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if str(id) == "1" :
            id = "serkan"
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,str(id),(x,y+h),font,1,(255,0,0))
            
        if str(id)== "2":
            id = "hairu"
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,str(id),(x,y+h),font,1,(255,0,0))
            
        
        
        dondurx(int(((x +(w/2))*(-78/640))+105))
        dondury(int(((y -(h/2))*(-57/480))+122))
        
        val = (x +(w/2))
        print(val/5)
        
    cv2.imshow("Face",img)
    if(cv2.waitKey(25)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()



