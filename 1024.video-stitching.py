#
# @lc app=leetcode id=1024 lang=python3
#
# [1024] Video Stitching
#

# @lc code=start
from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # 1. 按 start 升序排序；如果 start 相同，可以让 end 大的排在前面（非必需）
        clips.sort(key=lambda x: (x[0], -x[1]))
        
        cur_end = 0      # 当前覆盖最远端
        next_end = 0     # 下一步能覆盖的最远端
        cnt = 0          # 选用的片段数量
        i = 0
        n = len(clips)
        
        # 当 cur_end < T 时，持续尝试延伸
        while cur_end < T:
            # 在所有 start <= cur_end 的片段里寻找能延伸到最远的 next_end
            while i < n and clips[i][0] <= cur_end:
                next_end = max(next_end, clips[i][1])
                i += 1
            
            # 如果无法再延伸，则覆盖失败
            if next_end == cur_end:
                return -1
            
            # 选用一次延伸
            cnt += 1
            cur_end = next_end
        
        return cnt

# @lc code=end

