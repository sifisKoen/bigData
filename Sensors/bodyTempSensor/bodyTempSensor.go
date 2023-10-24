package main

import (
	"fmt"
	"math/rand"
	"time"
)

func readFromBodyTempSensor() float64 {
	return 36.0 + rand.Float64()*2 // Example reading between 30C to 38C
}

func main() {
	for {
		fmt.Println("Body temp Sensor Reading: ", readFromBodyTempSensor(), "C")
		time.Sleep(5 * time.Second)
	}

}
