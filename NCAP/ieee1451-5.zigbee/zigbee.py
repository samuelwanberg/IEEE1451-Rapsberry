from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.util.utils import hex_to_string
from digi.xbee.devices import ZigBeeDevice
from digi.xbee.models.mode import APIOutputModeBit
from digi.xbee.util import utils
from datetime import date, datetime
from logs.logserver import NcapManagerLog


class ConnectZigBee:

    def __init__(self, port="/dev/ttyUSB0", baud_rate=9600):
        self.PORT = port
        self.BAUD_RATE = baud_rate
        self.timeout = 0.5
        self.connect()

        self.log = NcapManagerLog()

    def connect(self):
        try :
            self.device = XBeeDevice(self.PORT, self.BAUD_RATE)
            self.log.conn(self.device)
        except Exception:  
            self.log.error(self.device)
        
    def dicovery_node(self,  callback):

        try:
            self.device.open()
            xbee_network = self.device.get_network()
            xbee_network.set_discovery_timeout(15)  # 15 seconds.
            xbee_network.clear()
            xbee_network.add_device_discovered_callback(callback)
            xbee_network.start_discovery_process()
            #aplicar um servidor de logs locais print("Discovering remote XBee d
            # ou talvez registar os logs no callback
            while xbee_network.is_discovery_running():
                time.sleep(0.1)

        finally:
            if self.device is not None and self.device.is_open():
                self.device.close()
                
                
    def command_env_rec(self, command, mac, device):
        
        try:
            #talvez aqui aplicar threads
            xbee64 = XBee64BitAddress 
            remote = RemoteXBeeDevice(device, xbee64.form_hex_string(mac))
            device.send_data(remote, command)
            time_s = time.time()

            while (xbee_message is None) and time.time() < time_s + timeout:
                xbee_msg = device.read_data()

                if(xbee_message is not None):
                    return xbee_msg.data.decode()
                    
                else:
                    log = (xbee_msg.remote_device.get_64bit_addr(),  )
                    error_code
        except:
            error
            
    
    def send_command(self,command, mac):
        
        #talvez aqui tenhamos um probelmas a de se conferires
        #talvez criarmos um método para verificar se o zigbee esta alive 
        #self.device = ZigBeeDevice(self.PORT, self.BAUD_RATE)

        try:
            self.device.open()
            response = self.command_env_rec(mac, command, device)
            #Aqui espera-se um retorno para o padrão IEEE 1451
            #Aqui também aplicar logs para registar eventos do servidor
            if response:
                return response 
            else:
                return 'Error Code Message format'
        
        finally:
            if self.device is not None and self.device.is_open():
                self.device.close()
