# test Comms made for Calvin Mars Rover 2018-19
# by Jason Pruim and Joel Muyskens based on digi.xBee github

from digi.xbee.devices import XBeeDevice


def test_receive2(my_port, my_baud):
    # Start Test
    print("Start Receive Test 2 - Receive once")

    device = XBeeDevice(my_port, my_baud)
    print("Waiting for data...\n")
    device.open()
    # Read data.
    while True:
        xbee_message = device.read_data()
        if xbee_message:
            print(xbee_message.data.decode("utf-8"))
            break
    device.close()
    print("Receive Test 2 Complete")


if __name__ == '__main__':
    # values to be changed on different computers
    port = "COM3"
    baud = 19200
    test_receive2(port, baud)
