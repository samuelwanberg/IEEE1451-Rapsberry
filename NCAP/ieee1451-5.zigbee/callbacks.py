
from bd import *

class Calls:
    
    def __init__(self):
        self.macs = {}

    def discovery(remote):    
    
        # Connect database 
        # Consulta nos banco de dados todos os mac ja cadatrado 
        # Coloca tudo dentro de um dicioario 
        # veficar as informações para saber se o modulo ja estou cadatrado 
        #
        #extract mac from zigbee
        #acho que aqui deveria verificar o type do remote 
    
        mac, name = str(remote).strip.split('-')
        
        if not mac in self.macs:
            self.macs[mac] = name

        print(self.macs)
        
    def info(self):
        pass
