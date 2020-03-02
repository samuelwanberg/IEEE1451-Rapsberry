from redis import ConnectRedis
import json


class Store:

    def __init__(self, teds):
        self.teds = teds
        self.bd = 1

        all_teds = [
            'METATEDS',
            'CHANNEL'
            'PHYTEDS',
            'USERNAMETEDS',
            ]

    def json_validate(self):
        

    def connect(self):
        redis = ConnectRedis()
        
        if not redis.test():
            
