# from gpiozero import Robot
# importing the required modules
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# import pygame,sys
# from pygame.locals import *
# pygame.init()
from time import sleep

# SCREEN_SIZE = (500,500)
# screen = pygame.display.set_mode((SCREEN_SIZE))
# pygame.display.set_caption('Underwater Robot')
L1 = 14
L2 = 15
L3 = 2
L4 = 3

C1 = 10
C2 = 9
C3 = 11
C4 = 8

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if (GPIO.input(C1) == 1):
        return (characters[0])
    if (GPIO.input(C2) == 1):
        return (characters[1])
    if (GPIO.input(C3) == 1):
        return (characters[2])
    if (GPIO.input(C4) == 1):
        return (characters[3])
    GPIO.output(line, GPIO.LOW)


# robot = Robot(left=(4, 17), right=(18, 27)) #4 and 17 are the forward and backward pins of the left motor and
# 18 and 27 are the forward and backward pins of the right motor
# robot2 = Robot(left=(22, 23), right=(24, 25)) #22 and 23 are the forward and backward pins of the left motor and
# 24 and 25 are the forward and backward pins of the right motor
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
# print("W: Forward")
# print("S: Backward")
# print("A: Left")
# print("D: Right")
condition = True
while (condition):
    pressed = None
    pressed = readLine(L1, ["7", "8", "9", "/"])
    if pressed is None:
        pressed = readLine(L2, ["4", "5", "6", "*"])
    if pressed is None:
        pressed = readLine(L3, ["1", "2", "3", "-"])
    if pressed is None:
        pressed = readLine(L4, ["c", "0", "=", "+"])
    sleep(0.1)
    if (pressed == "8"):
        forward = True
        # print("Forward")
        # sleep(t)
    if (pressed == "2"):
        reverse = True
        # print("Backward")
    if (pressed == "4"):
        turn_left = True
        # print("Left")
    if (pressed == "6"):
        turn_right = True
        # print("Right")
    if pressed is None:
        forward = reverse = turn_left = turn_right = False
        GPIO.output([lw11, lw12, rw11, rw12], GPIO.LOW)
        GPIO.output([lw21, lw22, rw21, rw22], GPIO.LOW)
    if pressed == "5":
        condition = False

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
        sleep(1)
    GPIO.output(ledf, GPIO.LOW)
    GPIO.output(ledb, GPIO.LOW)
    GPIO.output(ledl, GPIO.LOW)
    GPIO.output(ledr, GPIO.LOW)
    # pygame.display.update()