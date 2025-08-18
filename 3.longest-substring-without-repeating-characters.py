#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, right = 0, 0
        max_len = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
        
# @lc code=end

