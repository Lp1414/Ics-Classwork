# Imports go at the top
from microbit import *

servoSpeed = 0
def set_servo_angle(pin, angle): # code taken from classroom
    duty = 26 + (angle * 102) / 180
    pin.write_analog(duty)
Crash_sensor = pin1      #crash sensor value

def waterShoot(cycle, time, level): # "cycle" is which direction the motor is rotating, "time" is how long the motor sleeps for before rotating again, "level" is the speed of the servo (the variable)
    servoSpeed = level   
    if cycle == 0:
        for i in range(2):
            display.show(Image.DIAMOND)
            sleep(time)
            set_servo_angle(pin0, 90)
            display.show(Image.DIAMOND_SMALL)
            sleep(time)
            set_servo_angle(pin0, 0)
            display.show(servoSpeed)
            servoSpeed = level
    elif cycle == 1:
        for i in range(2):
            servoSpeed = level
            display.show(Image.DIAMOND_SMALL)
            sleep(time)
            set_servo_angle(pin0, 0)
            display.show(Image.DIAMOND)
            sleep(time)
            set_servo_angle(pin0, 90)
            display.show(servoSpeed)
            servoSpeed = level
    
while True:
   
    
    if Crash_sensor.is_touched():
            servoSpeed = 1
            waterShoot(1, 1000, 1)
            servoSpeed = 1
    sleep(1000)
    set_servo_angle(pin0, 90)
    if button_a.is_pressed() and button_b.is_pressed():
            servoSpeed = 1
            waterShoot(1, 1000, 1)
            servoSpeed = 1
    is_touched_value = Crash_sensor.is_touched()
    
    