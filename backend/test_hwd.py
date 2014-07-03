import time
import threading
import logging
import socket
import pika
from blockytalky_id import *
from message import *
from BrickPi import *


#fanout 
parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(parameters)        
hwcmd_channel = connection.channel()
hwcmd_channel.exchange_declare(exchange='HwCmd', type='fanout')
"""

# non fanout
connection = pika.BlockingConnection(pika.ConnectionParameters())
hwcmd_channel = connection.channel()
hwcmd_channel.queue_declare(queue="HwCmd")

"""
toSend = Message("asdf", None, "HwCmd", Message.createImage(motor1=100))
toSend = Message.encode(toSend)
print toSend
        
       

while True:
    
    hwcmd_channel.basic_publish(exchange='HwCmd', routing_key='', body=toSend)
    time.sleep(2)
