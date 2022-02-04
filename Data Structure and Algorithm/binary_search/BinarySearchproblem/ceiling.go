package main

import "fmt"

//Find the smallest element in among greater or equal the target
func ceiling(arr []int, target int) int {
	l := 0                   //stating valu
	h := len(arr) - 1        // end value=array lenght - 1
	isAsc := arr[l] < arr[h] // check array number order
	for l <= h {             // check start value is small
		mid := l + (h - l) // find the middle valu of a array

		if isAsc { //if array is assending order
			if target == arr[mid] { // if target value is queal to middle value *
				return arr[mid] // return mid value not index*
			} else if target > arr[mid] { // if target value is bigger then middle value *
				l = mid + 1 // new start  *
			} else {
				h = mid - 1 //new end*
			}
		} else { // if decendind*
			if target == arr[mid] { // if target value is queal to middle value *
				return arr[mid]
			} else if target > arr[mid] { // if target value is bigger then middle value *
				h = mid - 1 // new start  *
			} else { // if target value is lower then middle value *
				l = mid + 1 //new end*
			}
		}
	}
	return arr[l] // return next low value, after while loop condtion violated*
}

func main() { //main function*
	// Create an exmaple array and target
	// array := []int{9, 7, 5, 3, 1}
	array := []int{1, 4, 5, 7, 12, 16} //array value*
	target := 6                        //target value*
	// call function
	result := ceiling(array, target)
	// Print number of items
	fmt.Println(result)
}
