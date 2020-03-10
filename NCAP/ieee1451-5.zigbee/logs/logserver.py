import logging 
import digi.xbee.devices

class NcapManagerLog:

    def __init__(self):
        
        self.connFile = logger.FileHandler('syslog/conn.log')
        self.connFile.setLevel(logging.INFO)
        format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.connFile.setFormatter(format)

        self.errorfile = logger.FileHandler('syslog/error.log')
        self.errorfile.setLevel(logging.ERROR)
        format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.errorfile.setFormatter(format)

        self.accessfile = logger.FileHandler('syslog/access.log')
        self.accessfile.setLevel(logging.INFO)
        format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.accessfile.setFormatter(format)


    def conn(self, devices, msg):
        logger = logging.getLogger(devices.__name__)
        logger.addHandler(self.connFile)
        logger.INFO(msg)

    def error(self, msg):
        logger = logging.getLogger('ERROR')
        logger.addHandler(self.errorfile)
        logger.ERROR(msg)

    def access(self, msg):
        logger = logging.getLogger('ACCESS')
        logger.addHandler(self.accessfile)
        logger.INFO(msg)

