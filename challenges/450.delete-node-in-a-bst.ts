/*
* @lc app=leetcode id=450 lang=typescript
*
* [450] Delete Node in a BST
*
* https://leetcode.com/problems/delete-node-in-a-bst/description/
*
* algorithms
* Medium (50.81%)
* Likes:    8603
* Dislikes: 236
* Total Accepted:    436.8K
* Total Submissions: 858.3K
* Testcase Example:  '[5,3,6,2,4,null,7]\n3'
*
* Given a root node reference of a BST and a key, delete the node with the
* given key in the BST. Return the root node reference (possibly updated) of
* the BST.
* 
* Basically, the deletion can be divided into two stages:
* 
* 
* Search for a node to remove.
* If the node is found, delete the node.
* 
* 
* 
* Example 1:
* 
* 
* Input: root = [5,3,6,2,4,null,7], key = 3
* Output: [5,4,6,2,null,null,7]
* Explanation: Given key to delete is 3. So we find the node with value 3 and
* delete it.
* One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
* Please notice that another valid answer is [5,2,6,null,4,null,7] and it's
* also accepted.
* 
* 
* 
* Example 2:
* 
* 
* Input: root = [5,3,6,2,4,null,7], key = 0
* Output: [5,3,6,2,4,null,7]
* Explanation: The tree does not contain a node with value = 0.
* 
* 
* Example 3:
* 
* 
* Input: root = [], key = 0
* Output: []
* 
* 
* 
* Constraints:
* 
* 
* The number of nodes in the tree is in the range [0, 10^4].
* -10^5 <= Node.val <= 10^5
* Each node has a unique value.
* root is a valid binary search tree.
* -10^5 <= key <= 10^5
* 
* 
* 
* Follow up: Could you solve it with time complexity O(height of tree)?
* 
*/

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
    let parent: TreeNode | null = null;
    let curr: TreeNode | null = root;

    // Search for the node and its parent
    while (curr !== null) {
        if (curr.val === key) {
            break; // Found the node
        } else if (key > curr.val) {
            parent = curr;
            curr = curr.right;
        } else {
            parent = curr;
            curr = curr.left;
        }
    }

    // If the node wasn't found, return the root as-is
    if (curr === null) {
        return root;
    }

    // Handle deletion based on the number of children:

    // Node has no children (leaf node)
    if (curr.left === null && curr.right === null) {
        if (parent !== null) {
            if (parent.left === curr) {
                parent.left = null;
            } else {
                parent.right = null;
            }
        } else {
            root = null; // Handle deleting the root node
        }
        return root;
    }

    // Node has one child
    if (curr.left === null) {
        if (parent !== null) {
            if (parent.left === curr) {
                parent.left = curr.right;
            } else {
                parent.right = curr.right;
            }
        } else {
            root = curr.right; // Handle deleting the root node
        }
        return root;
    } else if (curr.right === null) {
        if (parent !== null) {
            if (parent.left === curr) {
                parent.left = curr.left;
            } else {
                parent.right = curr.left;
            }
        } else {
            root = curr.left; // Handle deleting the root node
        }
        return root;
    }

    // Node has two children
    let prev: TreeNode = curr;
    let successor: TreeNode = curr.right;

    // Find the in-order successor
    while (successor.left !== null) {
        prev = successor;
        successor = successor.left;
    }

    // Swap the values of the node and its successor
    curr.val = successor.val;

    // Delete the successor node
    if (prev.left === successor) {
        prev.left = successor.right;
    } else {
        prev.right = successor.right;
    }


    return root;
}

// @lc code=end

