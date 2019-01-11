# test Coms made for Calvin Mars Rover 2018-19
# by Jason Pruim and Joel Muyskens based on digi.xBee github

# imports
from digi.xbee.devices import*


def test_send1(my_port, my_baud):

    # Start Test
    print("Start Send Test 1 - Hello XBee World!")

    # Declare instance and Open Device Channel
    device = XBeeDevice(my_port, my_baud)
    device.open()
    # Instantiate an XBee device object.
    # Instantiate a remote XBee device object.
    remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A2004182DA22"))

    # Send data using the remote object.
    device.send_data_async(remote_device, "Hello XBee!")

    # send Data
    device.send_data_broadcast("Hello XBee World!")

    # Close device channel
    device.close()

    print("Send Test 1 Completed")


if __name__ == '__main__':
    # values to be changed on different computers
    port = "COM3"
    baud = 19200
    test_send1(port, baud)
