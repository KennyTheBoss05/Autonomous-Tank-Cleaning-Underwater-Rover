# from gpiozero import Robot
# importing the required modules
import math
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# import pygame,sys
# from pygame.locals import *
# pygame.init()
from time import sleep

# enter length of tank in cm
l = 150
# enter breadth of tank in cm
b = 150
# length and breadth of robot are 15cm and 15cm (say)
lrobot = 15
brobot = 15

ltank = math.floor(l / lrobot)
btank = math.floor(b / brobot)
# bottom left edge is (1,1) and bottom left edge of topright of the tank is (10,10) (in this case)

# enter the coordinates to clean
cor = [[3, 3], [3, 4], [4, 4], [5, 4], [6, 4], [6, 5], [7, 5]]

lw11 = 4
lw12 = 17
rw11 = 18
rw12 = 27
lw21 = 22
lw22 = 23
rw21 = 24
rw22 = 25
GPIO.setup([lw11, lw12, rw11, rw12, lw21, lw22, rw21, rw22], GPIO.OUT)
GPIO.output([lw11, lw12, rw11, rw12, lw21, lw22, rw21, rw22], GPIO.LOW)
fsensor = 5
bsensor = 6
lsensor = 12
rsensor = 13
ledf = 16
ledb = 19
ledl = 20
ledr = 26
check = 7
GPIO.setup(check, GPIO.OUT)
GPIO.setup([ledf, ledb, ledl, ledr], GPIO.OUT)
# GPIO.setup([fsensor,bsensor,lsensor,rsensor],GPIO.OUT)
GPIO.setup(fsensor, GPIO.IN)
GPIO.setup(bsensor, GPIO.IN)
GPIO.setup(lsensor, GPIO.IN)
GPIO.setup(rsensor, GPIO.IN)
forward = False
reverse = False
turn_left = False
turn_right = False

for i in range(0,len(cor)-1):
    #if(i == len(cor)-1):
    #    break
    if cor[i][0] - cor[i+1][0] == 1:
        turn_left = True
    if cor[i][0] - cor[i+1][0] == -1:
        turn_right = True
    if cor[i][1] - cor[i+1][1] == 1:
        reverse = True
    if cor[i][1] - cor[i+1][1] == -1:
        forward = True
    if forward:
        GPIO.output([lw11, rw12], GPIO.LOW)
        GPIO.output([lw12, rw11], GPIO.HIGH)
        GPIO.output([lw21, rw22], GPIO.LOW)
        GPIO.output([lw22, rw21], GPIO.HIGH)
    if reverse:
        GPIO.output([lw11, rw12], GPIO.HIGH)
        GPIO.output([lw12, rw11], GPIO.LOW)
        GPIO.output([lw21, rw22], GPIO.HIGH)
        GPIO.output([lw22, rw21], GPIO.LOW)
    if turn_left:
        GPIO.output([lw11, lw12, rw12], GPIO.LOW)
        GPIO.output(rw11, GPIO.HIGH)
        GPIO.output([lw21, lw22, rw22], GPIO.LOW)
        GPIO.output(rw21, GPIO.HIGH)
    if turn_right:
        GPIO.output([lw11, rw11, rw12], GPIO.LOW)
        GPIO.output(lw12, GPIO.HIGH)
        GPIO.output([lw21, rw21, rw22], GPIO.LOW)
        GPIO.output(lw22, GPIO.HIGH)
    sleep(1) #however long the wheels should run
    GPIO.output([lw11, lw12, rw11, rw12, lw21, lw22, rw21, rw22], GPIO.LOW)
    k = 0
    if (GPIO.input(fsensor) == GPIO.HIGH):
        GPIO.output(ledf, GPIO.HIGH)
        k = 1
    if (GPIO.input(bsensor) == GPIO.HIGH):
        GPIO.output(ledb, GPIO.HIGH)
        k = 1
    if (GPIO.input(lsensor) == GPIO.HIGH):
        GPIO.output(ledl, GPIO.HIGH)
        k = 1
    if (GPIO.input(rsensor) == GPIO.HIGH):
        GPIO.output(ledr, GPIO.HIGH)
        k = 1
    if k == 1:
        sleep(1) #however long the LED should glow
    GPIO.output(ledf, GPIO.LOW)
    GPIO.output(ledb, GPIO.LOW)
    GPIO.output(ledl, GPIO.LOW)
    GPIO.output(ledr, GPIO.LOW)

    forward = False
    reverse = False
    turn_left = False
    turn_right = False

