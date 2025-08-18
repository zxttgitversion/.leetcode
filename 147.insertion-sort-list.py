#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 空链表或单节点，直接返回
        if not head or not head.next:
            return head

        # 1. 虚拟头节点
        dummy = ListNode(float('-inf'))
        dummy.next = head

        # 2. 初始化已排序尾部和待插入节点
        last_sorted = head      # 已排序区最后一个节点
        curr = head.next        # 下一个待插入节点

        while curr:
            # 3. 如果 curr 本来 ≥ 已排序尾部，无需插入
            if curr.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                # 4. 否则需要找到插入位置：从 dummy 开始
                prev = dummy
                # 找到第一个值 > curr.val 的节点 prev.next
                while prev.next.val < curr.val:
                    prev = prev.next
                # 5. 插入 curr
                # 先断开 curr
                last_sorted.next = curr.next
                # 再接入到 prev 之后
                curr.next = prev.next
                prev.next = curr
            # 6. 移动 curr 到下一个待插入节点
            curr = last_sorted.next

        return dummy.next

# @lc code=end

