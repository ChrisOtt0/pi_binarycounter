from modules.binary_wrapper import BinaryWrapper
import sys

errmsg = "Unknown request. Please try again."
port1 = 18
port2 = 24
port3 = 12
port4 = 16

bw = BinaryWrapper(port1, port2, port3, port4)

def close():
    bw.zero()
    sys.exit()

functionality = {
    0: bw.zero,
    1: bw.one,
    2: bw.two,
    3: bw.three,
    4: bw.four,
    5: bw.five,
    6: bw.six,
    7: bw.seven,
    8: bw.eight,
    9: bw.nine,
    10: bw.ten,
    11: bw.eleven,
    12: bw.twelve,
    13: bw.thirteen,
    14: bw.fourteen,
    15: bw.fifteen,
    16: close
}

while True:
    num = 0
    try:
        num = int(input("Input a number between 0-15. 16 to exit: "))
    except:
        print(errmsg)
    
    if num > 16:
        print(errmsg)
    else:
        functionality[num]()
