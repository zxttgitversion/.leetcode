#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val  = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val   = val
#         self.left  = left
#         self.right = right

from typing import Optional, List

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 1. 链表转换为数组
        vals: List[int] = []
        p = head
        while p:
            vals.append(p.val)
            p = p.next
        
        # 2. 数组构造平衡 BST（复用 108 题模板）
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            # 中点作为根
            root = TreeNode(vals[mid])
            # 递归构造左右子树
            root.left  = build(left,     mid - 1)
            root.right = build(mid + 1,  right)
            return root
        
        return build(0, len(vals) - 1)

# @lc code=end

