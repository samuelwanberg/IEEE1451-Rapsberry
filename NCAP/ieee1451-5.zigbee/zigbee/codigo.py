#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Para instalar a biblioteca XBeeDevice
#comando: pip3 install digi-xbee
#Donwload do pacote de teste: git clone git@github.com:digidotcom/xbee-python.git
#Página de configuração: 
#https://xbplib.readthedocs.io/en/latest/getting_started_with_xbee_python_library.html#gsginstall

#Inicializar as tabelas do banco de dados
#ALTER TABLE `Nome da Tabela` AUTO_INCREMENT=0

from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.util.utils import hex_to_string
from digi.xbee.devices import ZigBeeDevice
from digi.xbee.models.mode import APIOutputModeBit
from digi.xbee.util import utils


import pymysql

import struct

#biblioteca de acesso aos módulos X-bee
from datetime import datetime
import numpy as np 

import random
import string

#bibliotecas para aquisição de tempo e conexão do banco de dados.
import time
import serial
import binascii
import pymysql
import struct
import codecs

import smbus
from ctypes import c_short
from ctypes import c_byte
from ctypes import c_ubyte
from datetime import date,datetime

import serial, time #this imports the libraries needed

import time 

#realiza a conexão com o banco de dados
try:
        # Abrimos uma conexão com o banco de dados:
        conexao = pymysql.connect(db='NCAPBD', user='root', passwd='ncapstim')
         
        # Cria um cursor:
        cursor = conexao.cursor()
except:
	   print ("Erro ao conectar ao banco de dados!!!\n")
 
#cursor.execute("INSERT INTO ESTACAO( MAC, NOM, VERSHARD, CODVER, PROTVERS) VALUES ('teste','teste','tes','tes','tes')")

# TODO: Replace with the serial port where your local module is connected to. 
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

timeout = 0.5

def Dicovery_node():

    device = XBeeDevice(PORT, BAUD_RATE)
    try:
        device.open()

        xbee_network = device.get_network()

        xbee_network.set_discovery_timeout(15)  # 15 seconds.

        xbee_network.clear()

        # Callback for discovered devices.
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
        
        #realiza a busca dos nós na rede retornando o endereço MAC
        xbee_network.add_device_discovered_callback(callback_device_discovered)

        xbee_network.add_discovery_process_finished_callback(callback_discovery_finished)

        xbee_network.start_discovery_process()

        print("Discovering remote XBee devices...")
        
        
        
        while xbee_network.is_discovery_running():
            time.sleep(0.1)

    finally:
        if device is not None and device.is_open():
            device.close()
    device.close()


def SendCommandEnvRec(res,dados,device):

    remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string(''+res))
            
    # Send data using the remote object.
    leit="0"
    try:
        device.send_data(remote_device, dados)
        #time.sleep(0.2)


        timeout_start = time.time()
        xbee_message = device.read_data()
        
        while (xbee_message is None) and time.time() < timeout_start + timeout:
              xbee_message = device.read_data()
              print (xbee_message)
              if (xbee_message is not None):
                 leit=str(float.fromhex(xbee_message.data.decode()))
                 print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),float.fromhex(xbee_message.data.decode())))
                 time.sleep(1)
    except:
        print ("Erro ao enviar o comando")
    return leit
               
def HoraAtual():
   hora_atual=str(datetime.now())
   hora_atual=hora_atual[11:19]
   return hora_atual
   
def DataAtual():
   data_atual = str(date.today())
   return data_atual
                  


def SendCommand():
   device = ZigBeeDevice(PORT, BAUD_RATE)
   
   #print(hora_atual[11:19])

   try:     
            
        device.open()
        device.flush_queues()
        cursor.execute("SELECT `MAC` FROM `ESTACAO`")
        resultado = cursor.fetchall()
        
        
        #verifica se o MAC já foi inserido no banco de dados
        for linha in resultado:
            res=str(linha)


            res=res[2:18]
            dados=("\x00\x01\x03\x01\x00\x04")
            leit=SendCommandEnvRec(res,dados,device)
            hora_atual=HoraAtual()
            data_atual=DataAtual()
            print ("Tempertura:"+leit)
            if leit!='0':
               cursor.execute("INSERT INTO `LEITURASENSOR`( `MACROT`, `CODSEN`, `DAT`, `HOR`, `VALO`) VALUES ('"+res+"',1,'"+data_atual+"','"+hora_atual+"','"+leit+"')")
               conexao.commit()
               #time.sleep(1)
            dados=("\x00\x02\x03\x01\x00\x04")
            leit=SendCommandEnvRec(res,dados,device)
            hora_atual=HoraAtual()
            data_atual=DataAtual()
            if leit!='0':
              leit="%.3f" % float(leit)
              print ("Pressão:"+leit)              
              cursor.execute("INSERT INTO `LEITURASENSOR`( `MACROT`, `CODSEN`, `DAT`, `HOR`, `VALO`) VALUES ('"+res+"',2,'"+data_atual+"','"+hora_atual+"','"+leit+"')")
              conexao.commit()
              #time.sleep(1)
            dados=("\x00\x03\x03\x01\x00\x04")
            leit=SendCommandEnvRec(res,dados,device)
            print ("Umidade:"+leit)
            hora_atual=HoraAtual()
            data_atual=DataAtual()
            if leit!='0':
              cursor.execute("INSERT INTO `LEITURASENSOR`( `MACROT`, `CODSEN`, `DAT`, `HOR`, `VALO`) VALUES ('"+res+"',3,'"+data_atual+"','"+hora_atual+"','"+leit+"')")
              conexao.commit()
              #time.sleep(1)
            dados=("\x00\x00\x01\x02\x00\x01\x01")
            leit=SendCommandEnvRec(res,dados,device)
              
                     
                    

   finally:
        if device is not None and device.is_open():
           device.close()


def main():
	while 1:
         print(" +--------------------------------------+")
         print(" | XBee Python Library Send Data Sample |")
         print(" +--------------------------------------+\n")
         print(" +--------------------------------------+")
         print(" 1 - Discovery Channel")
         print(" 2 - Send a command")
         print(" +--------------------------------------+\n")
         argument = input("Digite um valor: ")
         if argument == "1":
             Dicovery_node()
         elif argument=="2":
              SendCommand()
                   
                    

if __name__ == '__main__':
    main()
 
# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()
# Finaliza a conexão
conexao.close()
