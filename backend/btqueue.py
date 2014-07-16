import pika
import logging

class BTQueue(object):
    logging.basicConfig()
    def __init__(self, queue_name):
        self.queue_name = queue_name

    def publish(self, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', type='fanout')
        channel.basic_publish(exchange='logs', routing_key='', body=message)
        connection.close()

    def subscribe(self, callback):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', type='fanout')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='logs', queue=queue_name)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)
        channel.start_consuming()