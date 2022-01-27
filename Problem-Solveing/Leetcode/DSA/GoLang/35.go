// 35. Search Insert Position | 27/01/2022
// Problem Link: https://leetcode.com/problems/search-insert-position/
// Runtime: 4 ms, faster than 80.99% of Go online submissions for Search Insert Position.
// Memory Usage: 3 MB, less than 49.05% of Go online submissions for Search Insert Position.
package main

import "fmt"

func searchInsert(nums []int, target int) int {
	low := 0
	hight := len(nums) - 1
	for hight >= low {
		mid := low + ((hight - low) / 2)
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			hight = mid - 1
		} else {
			low = mid + 1
		}
	}
	return low
}
func main() {
	arr := []int{1, 3, 5, 6}
	target := 5
	res := searchInsert(arr, target)
	fmt.Println(res)
}
