#!/usr/bin/env python

import time
import thread
import logging
import socket
import usercode
import pika
import atexit
from blockytalky_id import *
from message import *
import urllib2

logger = logging.getLogger(__name__)


def handle_logging(logger):
    # Set the logging level.
    handler = logging.handlers.RotatingFileHandler(filename='/home/pi/blockytalky/logs/user_script.log',
                                                   maxBytes=8192, backupCount=3)
    globalHandler = logging.handlers.RotatingFileHandler(filename='/home/pi/blockytalky/logs/master.log',
                                                         maxBytes=16384, backupCount=3)
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s: %(message)s',
                                  datefmt='%H:%M:%S %d/%m')
    handler.setFormatter(formatter)
    globalHandler.setFormatter(formatter)
    globalHandler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(globalHandler)
    logger.setLevel(logging.INFO)
        

class UserScript(object):
    def __init__(self):
        logger.info('Initializing user script object')
       
        self.hostname = BlockyTalkyID()
        self.robot = Message.initStatus()
        
        self.sensorStatus= Message.createSensorStatus()
        logger.debug(self.sensorStatus.values())

        self.hwval_channel = None
        self.hwcmd_channel = None

        parameters = pika.ConnectionParameters()
        self.connection = pika.BlockingConnection(parameters)
        
        self.setup_hwcmd_channel()
        self.setup_hwval_channel()      
        self.hwval_channel.start_consuming()
   
    def setup_hwcmd_channel(self):  
        self.hwcmd_channel = self.connection.channel()
        logger.info("Creating sensors exchange...")
        self.hwcmd_channel.exchange_declare(exchange='HwCmd', type='fanout')

    def setup_hwval_channel(self):
        self.hwval_channel = self.connection.channel()
        self.hwval_channel.exchange_declare(exchange='sensors', type='fanout')
        result = self.hwval_channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        self.hwval_channel.queue_bind(exchange='sensors', queue=queue_name)
        logger.info("Declaring HwVal callback...")
        self.hwval_channel.basic_consume(self.handle_hwval_delivery, queue=queue_name, no_ack=True)
    


    def handle_hwval_delivery(self, ch, method, properties, body):
        #print " [us] %r" % (body,)
        toSend = Message("asdf", None, "HwCmd", Message.createImage(motor1=100))
        toSend = Message.encode(toSend)

        self.hwcmd_channel.basic_publish(exchange='HwCmd', routing_key=''
                                         , body=toSend)
   
        
        message = Message.decode(body)
        hwDict = message.getContent()
        logger.debug('Updating the robot status: %s' % str(hwDict))
        
        # update value changes
        for key, valueList in hwDict.iteritems():
            for index, value in enumerate(valueList):
                if value is not None:
                    self.robot[key][index] = value
                    
        # there is unread data on all ports
        for sensor in self.sensorStatus:
            self.sensorStatus[sensor] = True
        
  

if __name__ == "__main__":

    handle_logging(logger)
    us = UserScript()
    
    """
    #starts up sensors channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='sensors', type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='sensors', queue=queue_name)

    channel.basic_consume(us.callback, queue=queue_name, no_ack=True)
    channel.start_consuming()
    """
