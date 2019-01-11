# test Comms made for Calvin Mars Rover 2018-19
# by Jason Pruim and Joel Muyskens based on digi.xBee github

# imports other tests from directory
from TestSend1 import *
from TestReceive2 import *


# if main program then define defaults and run 2 tests,
def test_comms2():
    # values to be changed on different computers
    port = "COM3"
    baud = 19200
    print("Start tests")
    test_receive2(port, baud)
    test_send1(port, baud)
    print("Tests Completed")


if __name__ == '__main__ ':
    test_comms2()

