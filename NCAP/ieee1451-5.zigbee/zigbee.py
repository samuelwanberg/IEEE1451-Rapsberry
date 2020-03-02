
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

'''
def callback_device_discovered(remote):
            print("Device discovered: %s" %remote)
            
            MAC=str(remote)
            MAC1=MAC.split(' -')
            MAC=str(MAC1[:1])
            MACS=str(MAC[2:18])
            MACST=""+MACS
            #realiza uma busca pelo MAC no banco de dados.
            cursor.execute("SELECT `MAC` FROM `ESTACAO` WHERE `MAC`='"+MACST+"'")
            resultado = cursor.fetchall()
            #verifica se o MAC já foi inserido no banco de dados
            contrbanc=0
            for linha in resultado:
                contrbanc=1
            if contrbanc == 0:
                try:
                        # TODO: Replace with the 64-bit address of the remote device.
                        REMOTE_DEVICE_ADDRESS = XBee64BitAddress.from_hex_string(""+MACST)
                        remote_xbee = RemoteXBeeDevice(device, x64bit_addr=REMOTE_DEVICE_ADDRESS)
                        
                        device.read_device_info()
                        print("Read device info of local device successfully")
                        remote_xbee.read_device_info()
                        print("Read device info of remote device successfully")

                        print("\nLocal:")
                        print(device.get_node_id())
                        print(device.get_hardware_version())
                        print(hex_to_string(device.get_firmware_version()))
                        print(device.get_protocol())
                        # Read the output power level.
                        #print(""+str(device.get_power_level()))

                        print("\nRemote:")
                        print(remote_xbee.get_node_id())
                        print(remote_xbee.get_hardware_version())
                        print(hex_to_string(remote_xbee.get_firmware_version()))
                        print(remote_xbee.get_protocol())
                        print("Teste-->"+str(device.get_parameter("DB")))


                        #ni = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 20)))
                        #device.set_parameter("NI", bytearray(ni, "utf8"))
                        #param = device.get_parameter("NI")
                        #assert (param.decode() == ni)

                        #ni = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 20)))
                        #remote_xbee.set_parameter("NI", bytearray(ni, "utf8"))
                        #param = remote_xbee.get_parameter("NI")
                        #assert (param.decode() == ni)

                        print("\nTest finished successfully")
                                
                
                        cursor.execute("INSERT INTO ESTACAO( MAC, NOM, VERSHARD, CODVER, PROTVERS) VALUES ('"+MACST+"','"+str(remote_xbee.get_node_id())+"','"+str(remote_xbee.get_hardware_version())+"','"+str(hex_to_string(remote_xbee.get_firmware_version()))+"','"+str(remote_xbee.get_protocol())+"')")
                        conexao.commit()
                        print ("MAC inserido!!!")
                finally:
                        if device is not None and device.is_open():
                                print("Não inseriu no banco de dados!!!")
            else:
                print ("MAC já inserido!!!")
            #AtualizaNode(MACST)

        # Callback for discovery finished.

def callback_discovery_finished(status):
            if status == NetworkDiscoveryStatus.SUCCESS:
                print("Discovery process finished successfully.")
            else:
                print("There was an error discovering devices: %s" % status.description)
'''

def callback_device_discovered(remote):
    MAC , host = str(remote).strip().split('-')
    print(MAC)
    print(host)

class ConnectZigBee:


    def __init__(self):
        self.PORT = "/dev/ttyUSB0"
        self.BAUD_RATE = 9600
        self.timeout = 0.5

    def connect(self):
        try :
            self.device = XBeeDevice(self.PORT, self.BAUD_RATE)
        except Exception:
            print('Erro de conexão zigbee')
        
    def Dicovery_node(self):

        try:
            self.device.open()
            xbee_network = self.device.get_network()
            xbee_network.set_discovery_timeout(15)  # 15 seconds.
            xbee_network.clear()

            #realiza a busca dos nós na rede retornando o endereço MAC
            xbee_network.add_device_discovered_callback(callback_device_discovered)
            #xbee_network.add_discovery_process_finished_callback(callback_discovery_finished)
            xbee_network.start_discovery_process()
            print("Discovering remote XBee devices...")
        
            while xbee_network.is_discovery_running():
                time.sleep(0.1)

        finally:
            if self.device is not None and self.device.is_open():
                self.device.close()
                
                
