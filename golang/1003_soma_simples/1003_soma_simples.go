package main

import (
	"fmt"
)

func main() {
	A := *new(int)
	B := *new(int)

	fmt.Scanf("%d", &A)
	fmt.Scanf("%d", &B)

	SOMA := A + B

	fmt.Printf("SOMA = %d\n", SOMA)
}
