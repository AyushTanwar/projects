# OpenCV Python program to detect cars in video frame 
# import libraries of python OpenCV  
import cv2 

  
# capture frames from a video 
cap = cv2.VideoCapture('video5.mp4') 
  
# Trained XML classifiers describes some features of some object we want to detect 
car_cascade = cv2.CascadeClassifier('cars.xml') 
  
# loop runs if capturing has been initialized. 
while True: 
    
    # reads frames from a video 
    ret, frames = cap.read() 
      
    # convert to gray scale of each frames 
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
      
  
    # Detects cars of different sizes in the input image 
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
    i =0
    # To draw a rectangle in each cars 
    for (x,y,w,h) in cars: 
        if i==0 :
            cv2.rectangle(frames,(x,y),(x+w,y+h),(204,204,0),2) 
            i=1
        elif i==1 :
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,128,255),2)
            i=2
        else :
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,255,255),2)
            i=0
        
  
   # Display frames in a window  
    cv2.imshow('video2', frames) 
      
    # Wait for Esc key to stop 
    if cv2.waitKey(33) == 27: 
        break
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows() 