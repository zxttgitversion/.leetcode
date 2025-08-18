#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or (t1.val != t2.val):
                return False
            
            if is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left):
                return True
            else:
                return False
        return is_mirror(root, root)

# @lc code=end

