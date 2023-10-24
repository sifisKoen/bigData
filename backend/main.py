import time
import pika


def connect_to_rabbit():
    # Define the connection parameters
    connection_params = pika.ConnectionParameters(
        host='my-rabbitmq',  # Replace with the hostname of your RabbitMQ container
        port=5672,            # Default RabbitMQ port
        credentials=pika.PlainCredentials('guest', 'guest')
    )

    # Create a connection to RabbitMQ
    connection = pika.BlockingConnection(connection_params)

    # Create a channel
    channel = connection.channel()
    return channel

if __name__ == "__main__":

    channel = connect_to_rabbit()

    # Declare the queue you want to consume from
    queue_name = 'ehealth_queue'
    channel.queue_declare(queue=queue_name)

    # Define a callback function to process incoming messages
    def callback(ch, method, properties, body):
        print(f"Received message: {body.decode('utf-8')}")

    # Start consuming messages
    print(f"Waiting for messages from {queue_name}. To exit, press Ctrl+C.")
    while True:
        # Set up the consumer
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        
        