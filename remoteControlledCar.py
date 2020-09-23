from bluedot import BlueDot
from gpiozero import Robot
from gpiozero import DistanceSensor
from time import sleep

remoteControl = BlueDot()
teslaCyber = Robot(left=(7, 8), right=(9, 10))
sensor = DistanceSensor(24, 23)
auto = False

def move(pos):
    if pos.top:
        teslaCyber.forward()
    elif pos.bottom:
        teslaCyber.backward()
    elif pos.right:
        teslaCyber.left()
    elif pos.left:
        teslaCyber.right()

def stop():
    teslaCyber.stop()
    
def getDistance():
    distance = sensor.distance
    print (distance)
    return distance

def selfDrive():
    drive = autonomousMode(False)
    turningLeft = False
    while drive:
        distance = getDistance()
        while distance <= 0.50:
            if not turningLeft:
                teslaCyber.left()
                turningLeft = True
            distance = getDistance()
        teslaCyber.forward()
        turningLeft = False
        drive = autonomousMode(False)
    teslaCyber.stop()
    
def autonomousMode(change=True):
    global auto
    
    if change:
        auto = not auto
    return auto

def beginSelfDrive():
    autonomousMode()
    selfDrive()
        
remoteControl.set_when_rotated(beginSelfDrive, True)
# remoteControl.set_when_double_pressed(selfDrive, True)
remoteControl.when_moved = move
remoteControl.when_pressed = move
remoteControl.when_released = stop
