#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # 1. 取先序第一个作为本层根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. 在中序中找到根的位置，分割左右子树
        idx = inorder.index(root_val)
        # 左子树的中序和右子树的中序
        left_in  = inorder[:idx]
        right_in = inorder[idx+1:]
        
        # 3. 根据左子树节点数切出先序的左右部分
        left_pre  = preorder[1: 1 + len(left_in)]
        right_pre = preorder[1 + len(left_in): ]
        
        # 4. 递归构建
        root.left  = self.buildTree(left_pre,  left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root
# @lc code=end

