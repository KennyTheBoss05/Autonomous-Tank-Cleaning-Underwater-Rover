#from gpiozero import Robot
#importing the required modules
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import pygame,sys
from pygame.locals import *
pygame.init()
from time import sleep

SCREEN_SIZE = (500,500)
screen = pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption('Underwater Robot')

#robot = Robot(left=(4, 17), right=(18, 27)) #4 and 17 are the forward and backward pins of the left motor and
# 18 and 27 are the forward and backward pins of the right motor
#robot2 = Robot(left=(22, 23), right=(24, 25)) #22 and 23 are the forward and backward pins of the left motor and
# 24 and 25 are the forward and backward pins of the right motor
lw11 = 4
lw12 = 17
rw11 = 18
rw12 = 27
lw21 = 22
lw22 = 23
rw21 = 24
rw22 = 25
GPIO.setup([lw11,lw12,rw11,rw12,lw21,lw22,rw21,rw22],GPIO.OUT)
GPIO.output([lw11,lw12,rw11,rw12,lw21,lw22,rw21,rw22],GPIO.LOW)
fsensor = 5
bsensor = 6
lsensor = 12
rsensor = 13
ledf = 16
ledb = 19
ledl = 20
ledr = 26
check = 7
GPIO.setup(check,GPIO.OUT)
GPIO.setup([ledf,ledb,ledl,ledr],GPIO.OUT)
#GPIO.setup([fsensor,bsensor,lsensor,rsensor],GPIO.OUT)
GPIO.setup(fsensor, GPIO.IN)
GPIO.setup(bsensor, GPIO.IN)
GPIO.setup(lsensor, GPIO.IN)
GPIO.setup(rsensor, GPIO.IN)
forward = False
reverse = False
turn_left = False
turn_right = False
#print("W: Forward")
#print("S: Backward")
#print("A: Left")
#print("D: Right")
condition = True
while(condition):
    for event in pygame.event.get():
        #GPIO.output(check,GPIO.HIGH)
        #keys = pygame.key.get_pressed()
        if event.type == KEYDOWN:
            if(event.key== K_w):
                forward = True
                #print("Forward")
                #sleep(t)
            if(event.key== K_s):
                reverse = True
                #print("Backward")
            if (event.key== K_a):
                turn_left = True
                # print("Left")
            if (event.key== K_d):
                turn_right = True
                # print("Right")
        if event.type == KEYUP:
            forward = reverse = turn_left = turn_right = False
            GPIO.output([lw11,lw12,rw11,rw12],GPIO.LOW)
            GPIO.output([lw21, lw22, rw21, rw22], GPIO.LOW)
        if event.type == QUIT:
            condition = False
            pygame.quit()
            sys.exit()
        if forward:
            GPIO.output([lw11,rw12],GPIO.LOW)
            GPIO.output([lw12,rw11],GPIO.HIGH)
            GPIO.output([lw21, rw22], GPIO.LOW)
            GPIO.output([lw22, rw21], GPIO.HIGH)
        if reverse:
            GPIO.output([lw11, rw12], GPIO.HIGH)
            GPIO.output([lw12, rw11], GPIO.LOW)
            GPIO.output([lw21, rw22], GPIO.HIGH)
            GPIO.output([lw22, rw21], GPIO.LOW)
        if turn_left:
            GPIO.output([lw11,lw12,rw12],GPIO.LOW)
            GPIO.output(rw11,GPIO.HIGH)
            GPIO.output([lw21, lw22, rw22], GPIO.LOW)
            GPIO.output(rw21, GPIO.HIGH)
        if turn_right:
            GPIO.output([lw11, rw11, rw12], GPIO.LOW)
            GPIO.output(lw12, GPIO.HIGH)
            GPIO.output([lw21, rw21, rw22], GPIO.LOW)
            GPIO.output(lw22, GPIO.HIGH)
        if (GPIO.input(fsensor)==GPIO.HIGH):
            GPIO.output(ledf,GPIO.HIGH)
        if (GPIO.input(bsensor)==GPIO.HIGH):
            GPIO.output(ledb,GPIO.HIGH)
        if (GPIO.input(lsensor)==GPIO.HIGH):
            GPIO.output(ledl,GPIO.HIGH)
        if (GPIO.input(rsensor)==GPIO.HIGH):
            GPIO.output(ledr,GPIO.HIGH)
        sleep(1)
        GPIO.output(ledf, GPIO.LOW)
        GPIO.output(ledb, GPIO.LOW)
        GPIO.output(ledl, GPIO.LOW)
        GPIO.output(ledr, GPIO.LOW)
        #pygame.display.update()



