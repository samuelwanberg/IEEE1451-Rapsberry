import logging 

loggin.basicConfig(level=logging.DEBUG)

class wtimManagerLog:

    def __init__(self):
        
        
    def connection(self, msg):
        self.filename = 'conection.log'
        logging.basicConfig(filename=self.filename, filemode='w' ,format='%(asctime)s -> ', level=logging.INFO)
        
    def errormsg(self, msg):
        self.filename = 'conection.log'
        logging.basicConfig(filename=self.filename, filemode='w' ,format='%(asctime)s -> ', level=logging.INFO)
        
    def ieee14510(self, msg):
        pass

    def registration(self):
        pass
    
