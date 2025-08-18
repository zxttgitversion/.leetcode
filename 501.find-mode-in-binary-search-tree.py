#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            vals.append(node.val)
            in_order(node.right)
        
        in_order(root)

        freq_map = Counter()
        for val in vals:
            if val in freq_map:
                freq_map[val] += 1
            else:
                freq_map[val] = 1

        max_freq = max(freq_map.values(), default=0)
        
        res = []
        for key, count in freq_map.items():
            if count == max_freq:
                res.append(key)

        return res

        
        
# @lc code=end

