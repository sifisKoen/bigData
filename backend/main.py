import time
import pika
import psycopg2

def add_data_to_db(message, cur):
    insert_data_query = """
            INSERT INTO body_temp (message) 
            VALUES (%s);
        """
    # Execute the SQL query to insert data
    cur.execute(insert_data_query, (message))

    # Commit the transaction
    print("Data inserted into 'body_temp' table successfully.")


def connect_to_rabbit():
    # Define the connection parameters
    connection_params = pika.ConnectionParameters(
        host='localhost',  # Replace with the hostname of your RabbitMQ container
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
    def callback(ch, method, properties, body, my_additional_argument):
        cur = my_additional_argument
        message = body.decode('utf-8')
        print(cur)
        add_data_to_db(message, cur)
        print(f"Added message: {message}")
        

    # connect to postgres
    # PostgreSQL connection parameters
    db_params = {
        'dbname': 'ehealth_db',
        'user': 'guest',
        'password': 'guest',
        'host': 'localhost',  # Replace with the hostname or IP of your PostgreSQL container
        'port': '5432'  # Default PostgreSQL port
    }

    # SQL query to create the 'body_temp' table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS body_temp (
        id SERIAL PRIMARY KEY,
        message TEXT
    );
    """
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**db_params)

        # Create a cursor
        cur = conn.cursor()

        # Execute the SQL query to create the table
        cur.execute(create_table_query)

        # Commit the transaction
        conn.commit()
        print("Table 'body_temp' created successfully.")
    except Exception as e:
        print("Error:", e)
    
    # Start consuming messages
    print(f"Waiting for messages from {queue_name}. To exit, press Ctrl+C.")
    my_additional_argument = cur
    while True:
        # Set up the consumer
        # channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        on_message_callback=lambda ch, method, properties, body: callback(ch, method, properties, body, my_additional_argument),
        channel.start_consuming()


                





        