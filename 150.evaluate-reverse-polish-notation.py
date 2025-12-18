#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s not in '+-*/':
                stack.append(int(s))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if s == '+':
                    stack.append(a + b)
                elif s == '-':
                    stack.append(a - b)
                elif s == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack.pop()
# @lc code=end

