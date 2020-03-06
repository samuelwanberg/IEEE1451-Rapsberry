
from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.util.utils import hex_to_string
from digi.xbee.devices import ZigBeeDevice
from digi.xbee.models.mode import APIOutputModeBit
from digi.xbee.util import utils
from datetime import date, datetime
from ctypes import c_short
from ctypes import c_byte
from ctypes import c_ubyte
import numpy as np 
import random
import string
import pymysql
import struct
import time
import serial
import binascii
import pymysql
import struct
import codecs
import smbus


def callback_device_discovered(remote):
    
    MAC, host = str(remote).strip().split('-')
    
    #verify with zigbee is database 

class ConnectZigBee:


    def __init__(self, port="/dev/ttyUSB0", baud_rate=9600):
        self.PORT = port
        self.BAUD_RATE = baud_rate
        self.timeout = 0.5
        self.connect()

    def connect(self):
        try :
            self.device = XBeeDevice(self.PORT, self.BAUD_RATE)
        except Exception:
            #Todo error deve ser trabado e registar um logs de erros aplica aqui servidor de logs  
            print('Erro de conexão zigbee')
        
    def dicovery_node(self,  callback):

        try:
            self.device.open()
            xbee_network = self.device.get_network()
            xbee_network.set_discovery_timeout(15)  # 15 seconds.
            xbee_network.clear()
            xbee_network.add_device_discovered_callback(callback_device_discovered)
            xbee_network.start_discovery_process()

            #aplicar um servidor de logs locais print("Discovering remote XBee devices...")
            # ou talvez registar os logs no callback
            while xbee_network.is_discovery_running():
                time.sleep(0.1)

        finally:
            if self.device is not None and self.device.is_open():
                self.device.close()
                
                
    def send_command_env_rec_ieee1451(self, mac, ):
        
        conncect_remote = RemoteXBeeDevice(self.device, )
    

    def send_command(self,command, mac):
        
        #talvez aqui tenhamos um probelmas a de se conferires
        #talvez criarmos um método para verificar se o zigbee esta alive 
        #self.device = ZigBeeDevice(self.PORT, self.BAUD_RATE)

        try:
            self.device.open()
            response = self.send_command_env_rec_ieee1451(command, mac, device)
            #Aqui espera-se um retorno para o padrão IEEE 1451
            #Aqui também aplicar logs para registar eventos do servidor
            if response:
                return response 
            else:
                return 'Error Code Message format'
        

        finally:
            if self.device is not None and self.device.is_open():
                self.device.close()
