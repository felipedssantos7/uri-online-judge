package main

import (
	"fmt"
)

func main() {
	A := *new(float64)
	B := *new(float64)

	fmt.Scanf("%f", &A)
	fmt.Scanf("%f", &B)

	MEDIA := ((A * 3.5) + (B * 7.5)) / 11

	fmt.Printf("MEDIA = %.5f\n", MEDIA)
}
