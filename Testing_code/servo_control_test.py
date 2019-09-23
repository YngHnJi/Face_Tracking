# servo_control_test.py

import sys
import time
import os
#for bottom servo, L 80, C 121, R 160 (pin 17, echo 1)
#for top servo, (pin 18, echo 2)


os.system('sudo ./servod')

#setting start up serrvo positions
#positions range from (50-250)
#GPIO 17 bottom GPIO 18 top

servo1 = 121
os.system("echo 1=%s > /dev/servoblaster" %servo1)
time.sleep(0.1)
servo2 = 121
os.system("echo 2=%s > /dev/servoblaster" %servo2)
time.sleep(0.1)

tic = 3

# Servo motor control part
# servo2 up and down, servo1 right and left
while(True):
    ctr = input("Enter: ")
    # up
    if (ctr == "w"):
        servo2 -= tic
        print("servo1 : %d, servo2 : %d" %(servo1, servo2))
        os.system("echo 2=%s > /dev/servoblaster" %servo2)
        time.sleep(0.01)
    # down
    elif(ctr == "s"):
        servo2 += tic
        print("servo1 : %d, servo2 : %d" %(servo1, servo2))
        os.system("echo 2=%s > /dev/servoblaster" %servo2)
        time.sleep(0.01)
    # left
    elif(ctr == "d"):
        servo1 -= tic
        print("servo1 : %d, servo2 : %d" %(servo1, servo2))
        os.system("echo 1=%s > /dev/servoblaster" %servo1)
        time.sleep(0.01)
    # right
    elif(ctr == "a"):
        servo1 += tic
        print("servo1 : %d, servo2 : %d" %(servo1, servo2))
        os.system("echo 1=%s > /dev/servoblaster" %servo1)
        time.sleep(0.01)