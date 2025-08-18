#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def getDepth(self, node: TreeNode, goLeft: bool) -> int:
        
        depth = 0
        while node:
            depth += 1
            node = node.left if goLeft else node.right
        return depth - 1
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        hl = self.getDepth(root, goLeft=True)
        hr = self.getDepth(root, goLeft=False)
        if hl == hr:
            return 2 ** (hl + 1) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# @lc code=end

