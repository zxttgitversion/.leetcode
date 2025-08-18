#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 1

        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            depth += 1

            
# @lc code=end

