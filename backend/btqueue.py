import pika
import logging

class BTQueue(object):
    logging.basicConfig()
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name

    def publish(self, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters())
        channel = connection.channel()
        channel.exchange_declare(exchange=self.exchange_name, type='fanout')
        channel.basic_publish(exchange=self.exchange_name, routing_key='', body=message)
        connection.close()

    def subscribe(self, callback):
        connection = pika.BlockingConnection(pika.ConnectionParameters())
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', type='fanout')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='logs', queue=queue_name)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)
        channel.start_consuming()

    def add_timeout(self, timeout_interval, callback):
        self.connection.add_timeout(timeout_interval, callback)