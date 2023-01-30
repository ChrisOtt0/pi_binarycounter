import RPi.GPIO as GPIO;
import time;

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(18, True)
GPIO.output(24, True)
GPIO.output(12, True)
GPIO.output(16, True)
time.sleep(2)
GPIO.output(18, False)
GPIO.output(24, False)
GPIO.output(12, False)
GPIO.output(16, False)
