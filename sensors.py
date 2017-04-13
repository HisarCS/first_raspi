import time
import pins
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def get_ultrasound(trig, echo):
    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)
    start = time.time()
    end = time.time()
    while not GPIO.input(echo):
        start = time.time()
    while GPIO.input(echo):
        end = time.time()
    dtime = end - start
    dist = dtime * 17150 #cm
    return dist

def get_right():
    return get_ultrasound(pins.right_trig, pins.right_echo)
def get_left():
    return get_ultrasound(pins.left_trig, pins.left_echo)
def get_front():
    return get_ultrasound(pins.front_trig, pins.front_echo)
    

