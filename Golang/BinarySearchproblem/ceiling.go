package main

import "fmt"

//Find the smallest element in among greater or equal the target
func ceiling(arr []int, target int) int {
	l := 0
	h := len(arr) - 1
	isAsc := arr[l] < arr[h]
	for l <= h {
		mid := l + (h-l)/2

		if isAsc {
			if target == arr[mid] {
				return arr[mid]
			} else if target > arr[mid] {
				l = mid + 1
			} else {
				h = mid - 1
			}
		} else {
			if target == arr[mid] {
				return arr[mid]
			} else if target > arr[mid] {
				h = mid - 1
			} else {
				l = mid + 1
			}
		}
	}
	return arr[l]
}

func main() {
	// Create an exmaple array and target
	// array := []int{9, 7, 5, 3, 1}
	array := []int{1, 4, 5, 7, 12, 16}
	target := 6
	// call function
	result := ceiling(array, target)
	// Print number of items
	fmt.Println(result)
}
