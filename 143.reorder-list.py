#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        stk = []
        # 1. 把所有节点依次入栈，栈顶就是链表的尾部节点
        p = head
        while p is not None:
            stk.append(p)
            p = p.next

        # 2. 再从头开始，对称地弹出尾部节点，插到当前节点之后
        p = head
        while p is not None:
            # 2.1 从栈顶取出“尾部”节点
            lastNode = stk.pop()
            # 2.2 暂存 p.next，因为后面要把它接回去
            next = p.next

            # 3. 结束条件：当“尾部”已经和“头部”相遇或交错时，就不用再插了
            #    - odd 个节点：最后会 lastNode == next（中心点只需出现一次）
            #    - even 个节点：最后会 lastNode.next == next（两条“指针”刚好交叉）
            if lastNode == next or lastNode.next == next:
                # 切断多余的链接，防止成环
                lastNode.next = None
                break

            # 4. 将 lastNode 插到 p 和 next 之间
            p.next = lastNode
            lastNode.next = next

            # 5. p 前进到 next，准备下一轮对称插入
            p = next


        
# @lc code=end

