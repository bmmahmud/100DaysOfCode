// even-odd - 1
package main

import "fmt"

func evenOdd() {
	var t, n int
	fmt.Scanln(&t)
	for i := 1; i <= t; i++ {
		fmt.Scan(&n)
		if n%2 == 0 {
			fmt.Println("even")
		} else {
			fmt.Println("odd")
		}
	}
}

func main() {
	fmt.Println("Even/odd:")
	evenOdd()
}
