#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 初始化快慢指针，都从 head 出发
        slow = fast = head

        # 只要 fast 和 fast.next 都不是 None，就可以继续走
        while fast and fast.next:
            slow = slow.next          # 慢指针走 1 步
            fast = fast.next.next     # 快指针走 2 步
            if slow is fast:          # 相遇了，说明有环
                return True

        # 循环结束前要么 fast 遇到 None，要么 fast.next 遇到 None，都说明已经到了链表末尾
        return False                   # 无环

        
# @lc code=end

