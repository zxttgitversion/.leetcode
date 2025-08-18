#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if not node:  # 空节点是有效的 BST
                return True
            if not (min_val < node.val < max_val):  # 节点值不在有效范围内
                return False
            # 递归检查左右子树
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
        
        # 初始范围为负无穷到正无穷
        return dfs(root, float('-inf'), float('inf'))
# @lc code=end

