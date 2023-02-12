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

servo_1.start(5)
servo_2.start(5)

sleepPause = 0.1

positions = [ 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 15.0, 12.5, 10.0, 7.5, 5.0 ]

try:

	while 1:

		for position in positions:

			servo_1.ChangeDutyCycle(position)
			servo_2.ChangeDutyCycle(position)

			time.sleep(sleepPause)

			if not(GPIO.input(button_pin)):
				print("Pressed")
			else:
				print("Released")	
				

		time.sleep(5)

except KeyboardInterrupt:

	GPIO.cleanup()
