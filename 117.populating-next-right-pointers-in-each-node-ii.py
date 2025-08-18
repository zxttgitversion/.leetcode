#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr:
            head = None
            prev = None
            while curr:
                for child in (curr.left, curr.right):
                    if child:
                        if not head:
                            head = child
                        if prev:
                            prev.next = child
                        prev = child
                curr = curr.next
            curr = head
        return root


        
# @lc code=end

