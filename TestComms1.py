# test Comms made for Calvin Mars Rover 2018-19
# by Jason Pruim and Joel Muyskens based on digi.xBee github


# imports other tests from directory
from TestSend1 import *
from TestReceive2 import *
import time


def test_comms1():
    # values to be changed on different computers
    port = "COM3"
    baud = 19200
    print("Start tests")
    time.sleep(3)
    test_send1(port, baud)
    test_receive2(port, baud)
    print("Tests Completed")
# if main program then define defaults and run 2 tests,


if __name__ == '__main__':
    test_comms1()
