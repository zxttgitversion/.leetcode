#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from collections import Counter

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        left, right = 0, 0     # 滑动窗口 [left, right) `[0, 0)`
        start = 0              # 最小窗口起始位置
        min_len = float('inf') # 最小窗口长度
        valid = 0              # 满足条件的字符种类数

        while right < len(s):
            # 扩展右边界
            window[s[right]] += 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                valid += 1
            right += 1

            while valid == len(need):
                # 更新最小覆盖子串
                if right - left < min_len:
                    start = left
                    min_len = right - left

                # 左边界收缩
                if s[left] in need:
                    if window[s[left]] == need[s[left]]:
                        valid -= 1
                    window[s[left]] -= 1
                left += 1


        if min_len == float('inf'):
            return ''
        else:
            return s[start : start + min_len]

# @lc code=end

