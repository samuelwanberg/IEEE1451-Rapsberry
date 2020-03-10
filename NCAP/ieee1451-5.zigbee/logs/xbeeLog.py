
import logging


class xBeeLogger:

    def __init__(self):

        dev_logger = loggin.getLonger(digi.xbee.devices.__name__)
        handler = logging.StreamHandler()
        formatter = loggin.Formatter('%(asctime)s - %(name)s - %(levelname)s - ''%(message)s')
        handler.setFormatte


        dev_logger.addHandler(handler)

        
