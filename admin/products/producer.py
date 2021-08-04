# amqps://zjdufacy:NtlhbiXGSBHB-Nl3OAXenS66bWKJcTO0@clam.rmq.cloudamqp.com/zjdufacy
import pika, json

params = pika.URLParameters('amqps://zjdufacy:NtlhbiXGSBHB-Nl3OAXenS66bWKJcTO0@clam.rmq.cloudamqp.com/zjdufacy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)