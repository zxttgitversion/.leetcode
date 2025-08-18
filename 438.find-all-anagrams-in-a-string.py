#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return []
        
        need = Counter(p)
        window = Counter()
        left, right = 0, 0
        valid_len = len(p)

        while right < len(s):
            window[s[right]] += 1
            right += 1

            while right - left > valid_len:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            
            if window == need:
                res.append(left)

        return res

        

        # @lc code=end

