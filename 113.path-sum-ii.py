#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, remaining, path, res):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and remaining == node.val:
                res.append(list(path))
            remaining -= node.val

            dfs(node.left, remaining, path, res)
            dfs(node.right, remaining, path, res)

            path.pop()
        
        
        res = []
        path = []
        dfs(root, targetSum, path, res)
        return res
# @lc code=end

