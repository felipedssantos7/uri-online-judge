package main

import (
	"fmt"
)

func main() {
	num_func := *new(int)
	horas := *new(int)
	valor_hora := *new(float64)

	fmt.Scanln(&num_func)
	fmt.Scanln(&horas)
	fmt.Scanln(&valor_hora)

	horasFloat64 := float64(horas)
	salario := horasFloat64 * valor_hora

	fmt.Printf("NUMBER = %d\n", num_func)
	fmt.Printf("SALARY = U$ %.2f\n", salario)
}
