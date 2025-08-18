#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start):
            if start == len(s):
                res.append(list(path))
                return
            
            for end in range(start, len(s)):
                if is_palindrome(s[start : end + 1]):
                    path.append(s[start : end + 1])
                    backtrack(end + 1)
                    path.pop()
                    


        res = []
        path = []
        backtrack(0)
        return res
# @lc code=end

