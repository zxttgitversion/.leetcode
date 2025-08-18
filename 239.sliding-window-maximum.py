#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        res = []
        deq = deque()
        left, right = 0, 0

        while right < n:
            while deq and nums[right] > nums[deq[-1]]:
                deq.pop()
            deq.append(right)
            right += 1

            if right - left == k:
                res.append(nums[deq[0]])
                if deq[0] == left:
                    deq.popleft()
                left += 1
        
        return res




# @lc code=end

