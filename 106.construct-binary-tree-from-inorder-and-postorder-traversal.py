#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        
        # 1. 取先序第一个作为本层根节点
        root_val = postorder[-1]
        root = TreeNode(root_val)
        
        # 2. 在中序中找到根的位置，分割左右子树
        idx = inorder.index(root_val)
        # 左子树的中序和右子树的中序
        left_in  = inorder[:idx]
        right_in = inorder[idx+1:]
        
        # 3. 根据左子树节点数切出先序的左右部分
        left_post  = postorder[0: len(left_in)]
        right_post = postorder[len(left_in): -1]
        
        # 4. 递归构建
        root.left  = self.buildTree(left_in,  left_post)
        root.right = self.buildTree(right_in, right_post)
        return root 
# @lc code=end

