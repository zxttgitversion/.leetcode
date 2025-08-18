#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        has_odd = False

        for count in freq.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                has_odd = True
        
        if has_odd:
            return length + 1
        else:
            length
# @lc code=end

