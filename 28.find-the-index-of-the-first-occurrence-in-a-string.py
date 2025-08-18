#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
from typing import List
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        def build_lps(pattern: str) -> List[int]:
            lps = [0] * len(pattern)
            length = 0

            for i in range(1, len(pattern)):
                while length > 0 and pattern[i] != pattern[length]:
                    length = lps[length - 1]

                if pattern[i] == pattern[length]:
                    length += 1

                lps[i] = length

            return lps
        
        lps = build_lps(needle)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[jn]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1


        
# @lc code=end

