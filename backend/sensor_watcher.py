#!/usr/bin/env python
import pika

def say_still_listening():
    print "...Still listening..."
    connection.add_timeout(2, say_still_listening)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='sensors',
                         type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='sensors',
                   queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

channel.basic_consume(callback,
                      queue=queue_name, 
                      no_ack=True)

connection.add_timeout(1, say_still_listening)
channel.start_consuming()