import numpy as np
import cv2
from picarx import Picarx
import time
import subprocess  

px = Picarx()  
# Capturing video through webcam
webcam = cv2.VideoCapture(0)
  
# Start a while loop
while(1):
      
    _, imageFrame = webcam.read()
  
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
  
    # Set range for red color and 
    # define mask
    # lower_red = np.array([160,50,50],np.uint8)
    # upper_red = np.array([180,255,255],np.uint8)
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    # red_mask = cv2.inRange(hsvFrame, lower_red, upper_red)
  
    # Set range for green color and 
    # define mask
    # green_lower = np.array([25, 52, 72], np.uint8)
    # green_upper = np.array([102, 255, 255], np.uint8)
    lower_green = np.array([50, 100, 100], np.uint8)
    upper_green = np.array([70, 255, 255], np.uint8)
      
    # green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    green_mask = cv2.inRange(hsvFrame, lower_green, upper_green)
  
    # Set range for blue color and
    kernel = np.ones((5, 5), "uint8")
      
    # For red color
    red_mask = cv2.dilate(red_mask, kernel)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, 
                              mask = red_mask)
      
    # For green color
    green_mask = cv2.dilate(green_mask, kernel)
    res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                mask = green_mask)

    green_detect = np.sum(green_mask)
    red_detect = np.sum(red_mask)
    
    if green_detect > 0:
        print('Green detected!')
        subprocess.run(["python3", "Lane_extract.py"])
        ''''for angle in range(0,35):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35,0):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(0,35):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35,0):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)'''
    elif red_detect > 0:
        print('Red detected!')
    else:
        print('no color')
             
    # Program Termination
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
