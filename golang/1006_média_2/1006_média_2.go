package main

import (
	"fmt"
)

func main() {
	A := *new(float64)
	B := *new(float64)
	C := *new(float64)

	fmt.Scanln(&A)
	fmt.Scanln(&B)
	fmt.Scanln(&C)

	MEDIA := ((A * 2) + (B * 3) + (C * 5)) / 10

	fmt.Printf("MEDIA = %.1f\n", MEDIA)
}
