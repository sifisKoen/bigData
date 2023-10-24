package main

import (
	"fmt"
	"log"
	"math/rand"
	"time"

	"github.com/streadway/amqp"
)

func readFromBodyTempSensor() float64 {
	return 36.0 + rand.Float64()*2 // Example reading between 30C to 38C
}

func main() {
	rabbitMQHost := "my-rabbitmq" // Replace with the hostname or IP of your RabbitMQ server
	rabbitMQURL := fmt.Sprintf("amqp://guest:guest@%s:5672/", rabbitMQHost)

	conn, err := amqp.Dial(rabbitMQURL)
	if err != nil {
		log.Fatalf("Failed to connect to RabbitMQ: %v", err)
		return
	}
	defer conn.Close()
	ch, err := conn.Channel()

	if err != nil {
		log.Fatalf("Failed to open a channel: %v", err)
		return
	}
	defer ch.Close()

	queueName := "ehealth_queue"

	_, err = ch.QueueDeclare(
		queueName, // Queue name
		false,     // Durable
		false,     // Delete when unused
		false,     // Exclusive
		false,     // No-wait
		nil,       // Arguments
	)
	if err != nil {
		log.Fatalf("Failed to declare the ehealth_queue: %v", err)
		return
	}

	fmt.Printf("The 'ehealth_queue' has been successfully declared on the RabbitMQ server.\n")

	for {

		var message = fmt.Sprintf("%f", readFromBodyTempSensor())

		// Publish the message to the queue
		err = ch.Publish(
			"",        // Exchange
			queueName, // Routing key
			false,     // Mandatory
			false,     // Immediate
			amqp.Publishing{
				ContentType: "text/plain",
				Body:        []byte(message),
			},
		)

		if err != nil {
			log.Fatalf("Failed to publish a message: %v", err)
			return
		}

		log.Printf("Sent: %s", message)

		fmt.Println("Body temp Sensor Reading: ", readFromBodyTempSensor(), "C")
		time.Sleep(5 * time.Second)
	}

}
