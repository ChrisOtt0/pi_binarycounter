from modules.binary_wrapper import BinaryWrapper
import time

port1 = 18
port2 = 24
port3 = 12
port4 = 16

bw = BinaryWrapper(port1, port2, port3, port4)

bw.test()
time.sleep(10)
bw.off()
