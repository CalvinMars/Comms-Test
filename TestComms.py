#test Comms made for Calvin Mars Rover 2018-19
#by Jason Pruim and Joel Muyskens based on digi.xBee github
#imports other tests from directory
import TestSend1
import TestReceive2

# if main program then define defaults and run 2 tests,
if __name__ ==__main__:
    # values to be changed on different computers
    port = "COM3"
    baud = 19200
    print("Start tests")
    test_send1(port, baud)
    test_receive2(port,baud)
    print("Tests Completed")
