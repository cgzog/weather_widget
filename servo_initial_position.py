#
#	Set the servos to a known position for installing the pointers
#
#	After running this, the servos shoudl be positioned to install the pointers pointing fully to the right
#

import RPi.GPIO as GPIO
import time

GPIO.cleanup()


servo_pin_1 = 18
servo_pin_2 = 23

button_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_1, GPIO.OUT)
GPIO.setup(servo_pin_2, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

servo_1 = GPIO.PWM(servo_pin_1, 50) # GPIO 17 for PWM with 50Hz
servo_2 = GPIO.PWM(servo_pin_2, 50) # GPIO 23 for PWM with 50Hz

servo_1.start(7.5)
servo_2.start(7.5)

