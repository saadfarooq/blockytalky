import pika
import logging

class BTQueue(object):
    def __init__(self):
        logging.basicConfig()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="HwVal")

    def publish(self, message, routing_key):
        self.channel.basic_publish(exchange='',
                                   routing_key=routing_key,
                                   body=message)

    def subscribe(self, callback):
        self.channel.basic_consume(callback, queue="HwVal", no_ack=True)
        
    def close():
        self.channel.close()
        self.connection.close()