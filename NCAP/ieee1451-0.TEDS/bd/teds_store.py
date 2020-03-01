from redis import ConnectRedis
import json


class Store:

    def __init__(self, teds):
        self.teds = teds
        self.bd = 1

    def json_validate(self):
        
