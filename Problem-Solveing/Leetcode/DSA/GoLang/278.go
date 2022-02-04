// 278. First Bad Version | 02/02/2022
// Problem Link: https://leetcode.com/problems/first-bad-version/
// Runtime: 0 ms
// Memory Usage: 2 MB

// func firstBadVersion(n int) int {
// 	l := 1
// 	h := n
// 	result := n
// 	for l <= h {
// 		mid := (h + l) / 2
// 		if isBadVersion(mid) {
// 			result = mid
// 			h = mid - 1
// 		} else {
// 			l = mid + 1
// 		}
// 	}
// 	return result
// }