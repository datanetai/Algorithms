/*
 * @lc app=leetcode id=437 lang=golang
 *
 * [437] Path Sum III
 *
 * https://leetcode.com/problems/path-sum-iii/description/
 *
 * algorithms
 * Medium (46.97%)
 * Likes:    10642
 * Dislikes: 505
 * Total Accepted:    529.6K
 * Total Submissions: 1.1M
 * Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
 *
 * Given the root of a binary tree and an integer targetSum, return the number
 * of paths where the sum of the values along the path equals targetSum.
 *
 * The path does not need to start or end at the root or a leaf, but it must go
 * downwards (i.e., traveling only from parent nodes to child nodes).
 *
 *
 * Example 1:
 *
 *
 * Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
 * Output: 3
 * Explanation: The paths that sum to 8 are shown.
 *
 *
 * Example 2:
 *
 *
 * Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [0, 1000].
 * -10^9 <= Node.val <= 10^9
 * -1000 <= targetSum <= 1000
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func pathSum(root *TreeNode, targetSum int) int {
    prefixsum := make(map[int]int)
    return dfs(root, targetSum, 0, prefixsum)
}
prefixsum := make(map[int]int)
func dfs(node *TreeNode, targetSum int, foundSoFar int, prefixsum map[int]int) int {
    if node == nil {
        return 0
    }
    foundSoFar += node.Val
    count := 0
    if foundSoFar == targetSum {
        count++
    }
    if val, ok := prefixsum[foundSoFar-targetSum]; ok {
        count += val
    }
    prefixsum[foundSoFar]++
    count += dfs(node.Left, targetSum, foundSoFar, prefixsum)
    count += dfs(node.Right, targetSum, foundSoFar, prefixsum)
    prefixsum[foundSoFar]--
    return count
}

// @lc code=end

