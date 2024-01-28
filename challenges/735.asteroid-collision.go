/*
 * @lc app=leetcode id=735 lang=golang
 *
 * [735] Asteroid Collision
 *
 * https://leetcode.com/problems/asteroid-collision/description/
 *
 * algorithms
 * Medium (45.03%)
 * Likes:    7503
 * Dislikes: 931
 * Total Accepted:    445.8K
 * Total Submissions: 996K
 * Testcase Example:  '[5,10,-5]'
 *
 * We are given an array asteroids of integers representing asteroids in a
 * row.
 *
 * For each asteroid, the absolute value represents its size, and the sign
 * represents its direction (positive meaning right, negative meaning left).
 * Each asteroid moves at the same speed.
 *
 * Find out the state of the asteroids after all collisions. If two asteroids
 * meet, the smaller one will explode. If both are the same size, both will
 * explode. Two asteroids moving in the same direction will never meet.
 *
 *
 * Example 1:
 *
 *
 * Input: asteroids = [5,10,-5]
 * Output: [5,10]
 * Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never
 * collide.
 *
 *
 * Example 2:
 *
 *
 * Input: asteroids = [8,-8]
 * Output: []
 * Explanation: The 8 and -8 collide exploding each other.
 *
 *
 * Example 3:
 *
 *
 * Input: asteroids = [10,2,-5]
 * Output: [10]
 * Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
 * resulting in 10.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= asteroids.length <= 10^4
 * -1000 <= asteroids[i] <= 1000
 * asteroids[i] != 0
 *
 *
 */

// @lc code=start
func asteroidCollision(asteroids []int) []int {
	stack := []int{}
	for _, a := range asteroids {
		if a > 0 {
			stack = append(stack, a)
		} else {
			for len(stack) > 0 && stack[len(stack)-1] > 0 && stack[len(stack)-1] < abs(a) {
				stack = stack[:len(stack)-1]
			}
			if len(stack) == 0 || stack[len(stack)-1] < 0 {
				stack = append(stack, a)
			} else if stack[len(stack)-1] == -a {
				stack = stack[:len(stack)-1]
			}
		}
	}
	return stack
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

// @lc code=end

