#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node: TreeNode) -> bool:
            if not node:
                return 
            return node and not node.left and not node.right
        
        if not root:
            return 0
        
        l_total = 0
        if is_leaf(root.left):
            l_total += root.left.val

        return l_total + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

# @lc code=end

