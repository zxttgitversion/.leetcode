#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:  # 递归终止条件
                return None
            
            # 选择中间元素作为根节点
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # 构造左子树和右子树
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        # 从整个数组开始
        return helper(0, len(nums) - 1)
# @lc code=end

