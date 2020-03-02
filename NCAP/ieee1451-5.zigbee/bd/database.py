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

class Database:

    def __init__(self):
        try:
            # Abrimos uma conexão com o banco de dados:
            self.conexao = pymysql.connect(db='NCAPBD', user='root', passwd='ncapstim')
            # Cria um cursor:
            self.cursor = self.conexao.cursor()
	except Exception:   
            raise Exception("Erro ao conectar ao banco de dados!!!\n")
        
    
    
        
