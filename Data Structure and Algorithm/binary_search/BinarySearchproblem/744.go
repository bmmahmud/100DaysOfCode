package main

import (
	"fmt"
)

//Find the smallest element in among greater or equal the target
func ceiling(letters []byte, target byte) byte {

	l := 0                //stating valu
	h := len(letters) - 1 // end value=lettersay lenght - 1

	for l <= h { // check start value is small
		mid := l + (h-l)/2 // find the middle valu of a lettersay

		if target < letters[mid] { // if target value is bigger then middle value *
			h = mid - 1 //new end*
		} else {
			l = mid + 1 // new start  *
		}

	}
	return letters[l%len(letters)] // return next low value, after while loop condtion violated*
}

func main() { //main function*
	// Create an exmaple lettersay and target
	// lettersay := []int{9, 7, 5, 3, 1}
	lettersay := []byte{'c', 'f', 'j'} //lettersay value*
	var target byte = 'j'              //target value*
	// call function
	result := ceiling(lettersay, target)
	// Print number of items
	// fmt.Println(len(lettersay))
	fmt.Printf("Result: %c", result)
}
