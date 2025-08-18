#
# @lc app=leetcode id=2730 lang=python3
#
# [2730] Find the Longest Semi-Repetitive Substring
#

# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left, right = 0, 0
        count_pairs = 0
        max_len = 0

        while right < len(s):
            if right > 0 and s[right] == s[right - 1]:
                count_pairs += 1
            right += 1

            while count_pairs > 1:
                # 窗口是左闭右开 [left, right)，可用的索引是 left … right-1。
                # 要判断 s[left] == s[left+1]，必须保证 left+1 ≤ right-1
                if left + 1 <= right - 1 and s[left] == s[left + 1]:
                    count_pairs -= 1
                left += 1

            max_len = max(max_len, right - left)

        return max_len
# @lc code=end

