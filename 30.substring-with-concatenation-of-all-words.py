#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num = len(words)
        n = len(s)
        need = Counter(words)
        res = []

        # 对齐每一种偏移
        for offset in range(word_len):
            left = right = offset
            window = defaultdict(int)
            count = 0  # 已匹配的单词数

            # 以 word_len 为步长滑窗
            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len

                if word in need:
                    window[word] += 1
                    if window[word] <= need[word]:
                        count += 1
                    else:
                        # 出现多余，要不断收缩
                        while window[word] > need[word]:
                            lw = s[left:left + word_len]
                            window[lw] -= 1
                            if window[lw] < need[lw]:
                                count -= 1
                            left += word_len

                    # 全部单词都匹配上，记录起点并再收缩一个单词
                    if count == num:
                        res.append(left)
                        lw = s[left:left + word_len]
                        window[lw] -= 1
                        count -= 1
                        left += word_len

                else:
                    # 遇到无效单词，重置窗口
                    window.clear()
                    count = 0
                    left = right

        return res


# @lc code=end

