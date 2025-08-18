#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less_tail, greater_tail = less_dummy, greater_dummy

        curr = head
        while curr:
            if curr.val < x:
                less_tail.next= curr
                less_tail = less_tail.next
            else:
                greater_tail.next = curr
                greater_tail = greater_tail.next
            curr = curr.next

        greater_tail.next = None
        less_tail.next = greater_dummy.next
        return less_dummy.next
# @lc code=end

