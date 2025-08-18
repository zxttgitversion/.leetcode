#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            dummy = ListNode(0)
            dummy.next = head

            # 2. 初始化快慢指针，均指向 dummy
            fast = dummy
            slow = dummy

            # 3. fast 先走 k 步
            for _ in range(n):
                fast = fast.next

            # 4. 快慢同步移动，直到 fast 到达尾部
            while fast.next:
                fast = fast.next
                slow = slow.next

            # 5. slow.next 即为待删除节点，执行删除
            slow.next = slow.next.next

            # 6. 返回新的头节点
            return dummy.next
# @lc code=end

