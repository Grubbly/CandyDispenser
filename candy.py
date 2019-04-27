# Servo Control
import RPi.GPIO as GPIO
import time

enable = 18
forwardPin = 17
backwardPin = 4
buttonForwardPin = 15
buttonBackwardPin = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(enable, GPIO.OUT)
GPIO.output(enable, GPIO.HIGH)
time.sleep(0.1)
GPIO.setup(forwardPin, GPIO.OUT)
GPIO.setup(backwardPin, GPIO.OUT)
GPIO.setup(buttonForwardPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonBackwardPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        GPIO.output(forwardPin, GPIO.input(buttonForwardPin))
        GPIO.output(backwardPin, GPIO.input(buttonBackwardPin))
except KeyboardInterrupt:
    GPIO.output(forwardPin, GPIO.LOW)
    GPIO.output(backwardPin, GPIO.LOW)
    GPIO.cleanup()