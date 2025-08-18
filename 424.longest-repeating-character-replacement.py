#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26
        left, right = 0, 0
        ans = 0
        maxCount = 0

        while  right < len(s):
            idx = ord(s[right]) - ord('A')
            cnt[idx] += 1
            maxCount = max(maxCount, cnt[idx])
            right += 1

            while right - left - maxCount > k:
                cnt[ord(s[left]) - ord('A')] -= 1
                left += 1

            ans = max(ans, right - left)

        return ans


# @lc code=end

