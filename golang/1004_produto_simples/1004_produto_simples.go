package main

import (
	"fmt"
)

func main() {
	A := *new(int)
	B := *new(int)

	fmt.Scanf("%d", &A)
	fmt.Scanf("%d", &B)

	PROD := A * B

	fmt.Printf("PROD = %d\n", PROD)
}
