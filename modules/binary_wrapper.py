import RPi.GPIO
from .gpio_wrapper import GpioWrapper

class BinaryWrapper(GpioWrapper):
    port1 = 0
    port2 = 0
    port3 = 0
    port4 = 0

    def __init__(self, port1, port2, port3, port4):
        super().__init__()
        port1 = port1
        port2 = port2
        port3 = port3
        port4 = port4
        self.gpio.setup(port1, self.gpio.OUT)
        self.gpio.setup(port2, self.gpio.OUT)
        self.gpio.setup(port3, self.gpio.OUT)
        self.gpio.setup(port4, self.gpio.OUT)

    def test(self):
        self.gpio.output(self.port1, True)
        self.gpio.output(self.port2, True)
        self.gpio.output(self.port3, True)
        self.gpio.output(self.port4, True)

    def off(self):
        self.gpio.output(self.port1, False)
        self.gpio.output(self.port2, False)
        self.gpio.output(self.port3, False)
        self.gpio.output(self.port4, False)
        
