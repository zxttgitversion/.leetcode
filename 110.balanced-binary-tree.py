#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: TreeNode) -> int:
            if not node:
                return 0
            
            left_h = check(node.left)
            if left_h == -1:
                return -1
            right_h = check(node.right)
            if right_h == -1:
                return -1
            
            if abs(left_h - right_h) > 1:
                return -1
            
            return 1 + max(left_h, right_h)
        return check(root) != -1
        
# @lc code=end

