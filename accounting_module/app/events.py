
"""
Handle event-driven architecture for transaction processing.
"""

import pika

def publish_event(event_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='transaction_queue')
    channel.basic_publish(exchange='', routing_key='transaction_queue', body=event_data)
    connection.close()

def consume_event():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='transaction_queue')

    def callback(ch, method, properties, body):
        print(f"Received {body}")

    channel.basic_consume(queue='transaction_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
