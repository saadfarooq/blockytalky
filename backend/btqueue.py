import pika
import logging

class BTQueue(object):
    logging.basicConfig()
    def __init__(self, queue_name):
        self.queue_name = queue_name

    def __channel(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        channel = self.connection.channel()
        channel.queue_declare(queue=self.queue_name)
        return channel

    def __close(self):
        self.connection.close()

    def publish(self, message):
        self.__channel().basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=message)
        self.__close()

    def subscribe(self, callback):
        self.__channel().basic_consume(callback, queue=self.queue_name, no_ack=True)
        self.__close()