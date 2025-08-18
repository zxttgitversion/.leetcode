#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            vals.append(node.val)
            in_order(node.right)

        vals = []
        in_order(root)
        min_diff = float('inf')
        for i in range(1, len(vals)):
            min_diff = min(min_diff, vals[i] - vals[i - 1])
        return min_diff
# @lc code=end

