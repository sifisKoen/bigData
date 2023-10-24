package main

import (
	"fmt"
	"math/rand"
)

func readFromBloodSugarSensor() float64 {
	return 70.0 + rand.Float64()*40 // Example reading between 70 and 110 sugar level
}

func main() {
	fmt.Println("Blood Sugar Sensor Reading: ", readFromBloodSugarSensor(), "mg/dL")
}
