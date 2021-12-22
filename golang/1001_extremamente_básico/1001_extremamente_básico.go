package main

import (
	"fmt"
)

func main() {
	A := *new(int)
	B := *new(int)

	fmt.Scanln(&A)
	fmt.Scanln(&B)

	X := A + B

	fmt.Println("X =", X)
}
