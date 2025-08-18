
#
# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#

# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
from typing import List
import random
class Master:
     def guess(self, word: str) -> int:
        pass

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(w1: str, w2: str) -> int:
            cnt = 0
            for i in range(len(w1)):
                if w1[i] == w2[i]:
                    cnt += 1
            return cnt
                
        for _ in range(10):
            min_max_group = float('inf')
            guess = words[0]

            for w1 in words:
                cnt = [0] * 7
                for w2 in words:
                    if w1 != w2:
                        match_cnt = match(w1, w2)
                        cnt[match_cnt] += 1
                worst_case = max(cnt)
                if worst_case < min_max_group:
                    min_max_group = worst_case
                    guess = w1
                    
            res = master.guess(guess)
            if res == 6:
                return
            
            new_words = []
            for w in words:
                if match(w, guess) == res:
                    new_words.append(w)
            words = new_words

            
            
# @lc code=end

