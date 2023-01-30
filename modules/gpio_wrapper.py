import RPi.GPIO as GPIO

class GpioWrapper:
    gpio = GPIO

    def __init__(self):
        self.gpio.setmode(GPIO.BCM)
