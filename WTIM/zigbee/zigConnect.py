from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.util.utils import hex_to_string
import os, sys
import struct


class xBeeConnect:
    
    def __init__(self):
        
        # TODO: Replace with the serial port where your local module is connected to.
        self.PORT = "/dev/ttyS0"
        # TODO: Replace with the baud rate of your local module.
        self.BAUD_RATE = 9600
        self.device = None

    def connect(self):
        self.device = XBeeDevice(self.PORT, self.BAUD_RATE)

    def get(self, callback):
        try:
            self.device.open()    
            self.device.add_data_received_callback(callback)
    
        finally:
            if self.device is not None and device.is_open():
                self.device.close()

