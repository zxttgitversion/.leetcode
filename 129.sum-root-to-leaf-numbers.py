#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        q = deque([(root, root.val)])
        while q:
            node, curr = q.popleft()

            if not node.left and not node.right:
                total += curr
            else:
                if node.left:
                    q.append((node.left, curr*10 + node.left.val))
                if node.right:
                    q.append((node.right, curr*10 + node.right.val))
        return total
        
# @lc code=end

