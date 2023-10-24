package main

import (
	"fmt"
	"math/rand"
)

func readFromBodyTempSensor() float64 {
	return 36.0 + rand.Float64()*2 // Example reading between 30C to 38C
}

func main() {
	fmt.Println("Body temp Sensor Reading: ", readFromBodyTempSensor(), "C")
}
