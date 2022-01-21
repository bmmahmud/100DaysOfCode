package main

import "fmt"

func main() {
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}
	fmt.Println("Loop 1 Done")
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}
	fmt.Println("Loop 2 Done")
	for {
		fmt.Println("loop")
		break
	}
	fmt.Println("Loop 3 Done")
	for n := 0; n <= 5; n++ {
		if n%2 != 0 {
			continue
		}
		fmt.Println(n)
	}
	fmt.Println("Loop 4 Done")
}
