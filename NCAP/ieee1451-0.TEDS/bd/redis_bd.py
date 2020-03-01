
'''
  Use Redis for strore JSON Formats
'''
try:
    from redis import StrictRedis as BD
except ImportError:
    from redis import Redis as BD


class ConnectRedis(BD):

    def __init__(self, host='localhost', port=7000, db="WTIM"):
        
        self.db = {
            "WTIM": 0,
            "TEDS": 2,
            "TRANSDUCER": 3
        }[db]

        super().__init__(port=port, db=self.db)

        
    def autheticate(self):
        pass

    def test(self):
        return self.ping()

    def push(self, json):
        
        with self.pipeline() as pipe:
            pipe.multi()
            pipe.execute_command('JSON.SET', wtim, ',', json)
            pipe.execute()
            
    def query(self):
        pass
