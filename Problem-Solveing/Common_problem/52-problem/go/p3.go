// even-odd - 1
package main

import "fmt"

func printNum() {
	for i := 20; i >= 1; i-- {
		if i != 20 && i%5 == 0 {
			fmt.Println("")
		}
		fmt.Print(i, "\t")
	}
}

func main() {
	fmt.Println("Print:")
	printNum()
}
