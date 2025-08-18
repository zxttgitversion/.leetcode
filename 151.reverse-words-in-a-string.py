#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        def trim_spaces(s: list) -> list:
            slow, fast = 0, 0

            while fast < len(s) and s[fast] == ' ':
                fast += 1

            while fast < len(s):
                if s[fast] != ' ':
                    s[slow] = s[fast]
                    slow += 1
                elif s[fast] == ' ' and s[slow - 1] != ' ':
                    s[slow] = ' '
                    slow += 1
                fast += 1

            if slow > 0 and s[slow - 1] == ' ':
                slow -= 1

            return s[:slow]
        
        def reserve(s: List, left: int, right: int):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        def reserve_each_word(s: List):
            start = 0
            for end in range(len(s) + 1):
                if end == len(s) or s[end] == ' ':
                    reserve(s, start, end - 1)
                    start = end + 1

        s = list(s)
        s = trim_spaces(s)
        reserve(s, 0, len(s) - 1)
        reserve_each_word(s)
        return ''.join(s)


        
# @lc code=end

