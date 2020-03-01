
try:
    from redis import StrictRedis as BD
except ImportError:
    from redis import REdis as BD


class ConnectRedis(BD):

    def __init__(self, host='localhost', port=7000, bd=0):
        
        super().__init__(host=self.host, port=self.port, bd=self.bd)

        bd = {
            1: "TEDS",
            2: "WTIM",
            3: "TRANSDUERCHANNEL"
        }

    
    def autheticate(self):
        
    def test(self):
        return self.ping()

    
