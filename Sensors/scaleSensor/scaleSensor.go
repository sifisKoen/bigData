package main

import (
	"fmt"
	"math/rand"
)

func readFromScaleSensor() float64 {
	return 50.0 + rand.Float64()*10 // Example weight from 50.0 kg to 60.0kg
}

func main() {
	fmt.Println("Scale Sensor Reading: ", readFromScaleSensor(), "kg")
}
