# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, Dict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node :Optional[TreeNode],targetSum: int, soFar: int, prefixSum: Dict[int,int]) -> int:
            if node==None:
                return 0
            soFar += node.val
            count = 0
            if soFar==targetSum:
                count += 1
            count += prefixSum.get(soFar-targetSum,0)
            prefixSum[soFar] = prefixSum.get(soFar,0)+1
            count += dfs(node.left,targetSum,soFar,prefixSum)
            count += dfs(node.right,targetSum,soFar,prefixSum)
            prefixSum[soFar] -= 1
        
            return count
        
        return dfs(root,targetSum,0,{})
    
            


        