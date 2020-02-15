import os, sys
import numpy as np
import struct

#Bibliotecas do XBee
from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.util.utils import hex_to_string

import time
import serial
import binascii
import codecs

#importa as bibliotecas do sensor
import smbus
from ctypes import c_short
from ctypes import c_byte
from ctypes import c_ubyte


#Endereço do I2C
DEVICE = 0x76 # Default device I2C address

REMOTE_NODE_ID = "0000000000000000"

#comando de resposta baseado no IEEE 1451
commandresp=[0x01,0x00,0x02,0x00,0x13]

bus = smbus.SMBus(1) # Rev 2 Pi, Pi 2 & Pi 3 uses bus 1
                     # Rev 1 Pi uses bus 0
                     


# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyS0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

#funções para aquisição dos dados de temperatura, umidade e pressao
def getShort(data, index):
  # return two bytes from data as a signed 16-bit value
  return c_short((data[index+1] << 8) + data[index]).value

def getUShort(data, index):
  # return two bytes from data as an unsigned 16-bit value
  return (data[index+1] << 8) + data[index]

def getChar(data,index):
  # return one byte from data as a signed char
  result = data[index]
  if result > 127:
    result -= 256
  return result

def getUChar(data,index):
  # return one byte from data as an unsigned char
  result =  data[index] & 0xFF
  return result

def readBME280ID(addr=DEVICE):
  # Chip ID Register Address
  REG_ID     = 0xD0
  (chip_id, chip_version) = bus.read_i2c_block_data(addr, REG_ID, 2)
  return (chip_id, chip_version)

def readBME280All(addr=DEVICE):
  # Register Addresses
  REG_DATA = 0xF7
  REG_CONTROL = 0xF4
  REG_CONFIG  = 0xF5

  REG_CONTROL_HUM = 0xF2
  REG_HUM_MSB = 0xFD
  REG_HUM_LSB = 0xFE

  # Oversample setting - page 27
  OVERSAMPLE_TEMP = 2
  OVERSAMPLE_PRES = 2
  MODE = 1

  # Oversample setting for humidity register - page 26
  OVERSAMPLE_HUM = 2
  bus.write_byte_data(addr, REG_CONTROL_HUM, OVERSAMPLE_HUM)

  control = OVERSAMPLE_TEMP<<5 | OVERSAMPLE_PRES<<2 | MODE
  bus.write_byte_data(addr, REG_CONTROL, control)

  # Read blocks of calibration data from EEPROM
  # See Page 22 data sheet
  cal1 = bus.read_i2c_block_data(addr, 0x88, 24)
  cal2 = bus.read_i2c_block_data(addr, 0xA1, 1)
  cal3 = bus.read_i2c_block_data(addr, 0xE1, 7)

  # Convert byte data to word values
  dig_T1 = getUShort(cal1, 0)
  dig_T2 = getShort(cal1, 2)
  dig_T3 = getShort(cal1, 4)

  dig_P1 = getUShort(cal1, 6)
  dig_P2 = getShort(cal1, 8)
  dig_P3 = getShort(cal1, 10)
  dig_P4 = getShort(cal1, 12)
  dig_P5 = getShort(cal1, 14)
  dig_P6 = getShort(cal1, 16)
  dig_P7 = getShort(cal1, 18)
  dig_P8 = getShort(cal1, 20)
  dig_P9 = getShort(cal1, 22)

  dig_H1 = getUChar(cal2, 0)
  dig_H2 = getShort(cal3, 0)
  dig_H3 = getUChar(cal3, 2)

  dig_H4 = getChar(cal3, 3)
  dig_H4 = (dig_H4 << 24) >> 20
  dig_H4 = dig_H4 | (getChar(cal3, 4) & 0x0F)

  dig_H5 = getChar(cal3, 5)
  dig_H5 = (dig_H5 << 24) >> 20
  dig_H5 = dig_H5 | (getUChar(cal3, 4) >> 4 & 0x0F)

  dig_H6 = getChar(cal3, 6)

  # Wait in ms (Datasheet Appendix B: Measurement time and current calculation)
  wait_time = 1.25 + (2.3 * OVERSAMPLE_TEMP) + ((2.3 * OVERSAMPLE_PRES) + 0.575) + ((2.3 * OVERSAMPLE_HUM)+0.575)
  time.sleep(wait_time/1000)  # Wait the required time  

  # Read temperature/pressure/humidity
  data = bus.read_i2c_block_data(addr, REG_DATA, 8)
  pres_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
  temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
  hum_raw = (data[6] << 8) | data[7]

  #Refine temperature
  var1 = ((((temp_raw>>3)-(dig_T1<<1)))*(dig_T2)) >> 11
  var2 = (((((temp_raw>>4) - (dig_T1)) * ((temp_raw>>4) - (dig_T1))) >> 12) * (dig_T3)) >> 14
  t_fine = var1+var2
  temperature = float(((t_fine * 5) + 128) >> 8);

  # Refine pressure and adjust for temperature
  var1 = t_fine / 2.0 - 64000.0
  var2 = var1 * var1 * dig_P6 / 32768.0
  var2 = var2 + var1 * dig_P5 * 2.0
  var2 = var2 / 4.0 + dig_P4 * 65536.0
  var1 = (dig_P3 * var1 * var1 / 524288.0 + dig_P2 * var1) / 524288.0
  var1 = (1.0 + var1 / 32768.0) * dig_P1
  if var1 == 0:
    pressure=0
  else:
    pressure = 1048576.0 - pres_raw
    pressure = ((pressure - var2 / 4096.0) * 6250.0) / var1
    var1 = dig_P9 * pressure * pressure / 2147483648.0
    var2 = pressure * dig_P8 / 32768.0
    pressure = pressure + (var1 + var2 + dig_P7) / 16.0

  # Refine humidity
  humidity = t_fine - 76800.0
  #humidity = (hum_raw - (dig_H4 * 64.0 + dig_H5 / 16384.0 * humidity)) * (dig_H2 / 65536.0 * (1.0 + dig_H6 / 67108864.0 * humidity * (1.0 + dig_H3 / 67108864.0 * humidity)))
  #humidity = humidity * (1.0 - dig_H1 * humidity / 524288.0)
  #humidity = humidity * (1.0 - dig_H1 * humidity / 524288.0)
  '''if humidity > 100:
    humidity = 100
  elif humidity < 0:
    humidity = 0
    '''
  return temperature/100.0,pressure/100.0,humidity/1000


def main():
    print(" +-----------------------------------------+")
    print(" | XBee Python Library Receive Data Sample |")
    print(" +-----------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)
    #remote_device=RemoteXBeeDevice(device,XBee64BitAddress.from_hex_string(REMOTE_NODE_ID))

    try:
        device.open()

        def data_receive_callback(xbee_message):
            data=xbee_message.data
            command=[int.from_bytes(data[:2], "big"),int.from_bytes(data[2:3], "big"),int.from_bytes(data[3:4], "big"),int.from_bytes(data[5:6], "big"),int.from_bytes(data[6:7], "big")]
            print("Data[0]:",command[0])
            print("Data[1]:",command[1])
            print("Data[2]:",command[2])
            print("Data[3]:",command[3])
            print("Data[4]:",command[4])
            temperature,pressure,humidity = readBME280All()
           
            if command[1]==3:
                    if command[2]==1:
                        if command[0]==1:
                            #teste="teste2"
                            remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0000000000000000"))
                            print ("Temp      = {0:0.3f} Deg C",temperature,float.hex(temperature),float.fromhex(float.hex(temperature)))
                            # Send data using the remote object.
                            print("",float.fromhex(float.hex(temperature)))
                            print(""+float.hex(temperature))
                            device.send_data(remote_device, ''+float.hex(temperature))
                           
                        if command[0]==2:
                            print ("Press      = {0:0.3f}",pressure,float.hex(pressure),float.fromhex(float.hex(pressure)))
                            remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0000000000000000"))
                            # Send data using the remote object.
                            print("",float.fromhex(float.hex(pressure)))
                            print(""+float.hex(pressure))
                            device.send_data(remote_device, ''+float.hex(pressure))
                        if command[0]==3:
                            print ("Humity      = {0:0.3f} %",humidity,float.hex(humidity),float.fromhex(float.hex(humidity)))
                            remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0000000000000000"))
                            # Send data using the remote object.
                            print("",float.fromhex(float.hex(humidity)))
                            print(""+float.hex(humidity))
                            device.send_data(remote_device, ''+float.hex(humidity))
                        #if command[0]==4:
            if command[1]==1:
                    if command[2]==2:
                       if command[4]==1:
                          print ("Meta-TEDS")
                               
                           
        device.add_data_received_callback(data_receive_callback)
        print("Waiting for data...\n")
        input()

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()

