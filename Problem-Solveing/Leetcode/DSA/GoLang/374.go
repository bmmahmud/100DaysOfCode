// 374. Guess Number Higher or Lower
// https: //leetcode.com/problems/guess-number-higher-or-lower/submissions/
// Runtime: 2 ms, faster than 33.96% of Go online submissions for Guess Number Higher or Lower.
// Memory Usage: 1.9 MB, less than 99.37% of Go online submissions for Guess Number Higher or Lower.

// func guessNumber(n int) int {
// 	l, h := 1, n
// 	for l < h {
// 		mid := (l + h) / 2
// 		if guess(mid) == 1 {
// 			l = mid + 1
// 		} else {
// 			h = mid
// 		}
// 	}
// 	return l
// }