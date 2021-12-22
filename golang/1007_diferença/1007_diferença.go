package main

import (
	"fmt"
)

func main() {
	A := *new(int)
	B := *new(int)
	C := *new(int)
	D := *new(int)

	fmt.Scanln(&A)
	fmt.Scanln(&B)
	fmt.Scanln(&C)
	fmt.Scanln(&D)

	DIFERENCA := (A * B) - (C * D)

	fmt.Printf("DIFERENCA = %d\n", DIFERENCA)
}
