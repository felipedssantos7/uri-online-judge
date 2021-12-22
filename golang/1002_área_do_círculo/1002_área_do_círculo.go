package main

import (
	"fmt"
)

func main() {
	const PI = 3.14159
	raio := *new(float64)

	fmt.Scanln(&raio)

	area := PI * raio * raio

	fmt.Printf("A=%.4f\n", area)
}
