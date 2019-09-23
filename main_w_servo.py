# its main code

import cv2
import numpy as np
import sys
import os
import time
import login_sys
import face_detect
import face_id
import face_tracker

#setting start up serrvo positions
#positions range from (50-250)
#GPIO 17 bottom GPIO 18 top
#for bottom servo, L 80, C 121, R 160 (pin 17, echo 1)
#for top servo, D 160, C 121, H 100 (pin 18, echo 2)

os.system('sudo ./servod')

servo1 = 121
os.system("echo 1=%s > /dev/servoblaster" %servo1)
time.sleep(0.1)
servo2 = 121
os.system("echo 2=%s > /dev/servoblaster" %servo2)
time.sleep(0.1)

bbox_info = []
flag_unlocked = 0
model = cv2.face.LBPHFaceRecognizer_create()
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
tracker = cv2.TrackerMOSSE_create()

frame_width = 640
frame_height = 480

# it manage 
servo_movement = 1

# center coordinates of object
xValue = 0
yValue = 0

# Login-system // return: 1
login, username = login_sys.user_login_system()
print(username)

# Training model based on User info // return: training model
if login is True:
    Training_Data, Labels = face_id.Load_Training_data(username)
    model.train(np.asarray(Training_Data), np.asarray(Labels))

    print("Model Training Complete!!!!!")
else:
    print("Model Training Fail. Exit Program")
    sys.exit()

# Face Recognition // return: face image suitable for Face identification
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

if not video.isOpened():
    print("Video can't be opened, exit program")
    sys.exit()

# searching face to compare with training data
while(True):
    ret, frame = video.read()
    img, face, face_bbox = face_detect.face_detector_v2(frame)

    # Face identification // return: True, False
    if face is not None: # FACE DETECTED!
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display_string = str(confidence)+'% Confidence it is user'
        cv2.putText(frame,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)


        if confidence > 70: #unlock here if confidence more than 70
            cv2.putText(frame, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            #cv2.imshow('FaceFrame', frame)
            flag_unlocked = 1 # key to get in tracking part
            bbox_tracker = tuple(face_bbox[0]) # bounding box info saved here!
            print("Unlocked!")
            break

        else:
            cv2.putText(frame, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Frame', frame)

    else: # Any Face Not detected
        cv2.imshow("Frame", frame)

    cv2.waitKey(1)

cv2.destroyAllWindows()

# Face Tracking // return: tracking image
if (flag_unlocked == 1): # Face Tracking part
    tracker_ret = tracker.init(frame, bbox_tracker)

    while(True):
        ret, frame = video.read()

        tracker_ret, bbox_tracker = tracker.update(frame)

        if tracker_ret is True:
            # coordinates for Tracking, bounding box
            p1 = (int(bbox_tracker[0]), int(bbox_tracker[1]))
            p2 = (int(bbox_tracker[0] + bbox_tracker[2]), int(bbox_tracker[1] + bbox_tracker[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            # coordinates for servo control
            xValue = int(bbox_tracker[0]+bbox_tracker[2]/2)
            yValue = int(bbox_tracker[1]+bbox_tracker[3]/2)            
        
        # servo part
        if(  xValue > 380):
            if servo1 < 210:
                    servo1 += servo_movement
                    os.system("echo 1=%s > /dev/servoblaster" %servo1)
                    time.sleep(0.01)
        elif(xValue < 310):
            if servo1 > 50:
                    servo1 -= servo_movement
                    os.system("echo 1=%s > /dev/servoblaster" %servo1)
                    time.sleep(0.01)
    #y
        if( yValue < 200):
            if (servo2 < 210):
                    servo2 -= servo_movement
                    os.system("echo 2=%s > /dev/servoblaster" %servo2)
                    time.sleep(0.01)
        elif( yValue > 290):
            if (servo2 >50):
                    servo2 += servo_movement
                    os.system("echo 2=%s > /dev/servoblaster" %servo2)
                    time.sleep(0.01)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()



else:
    print("Something wrong")





