#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, segment, path):
            if segment == 4 and start == len(s):
                res.append('.'.join(path))
                return
            if segment == 4 or start == len(s):
                return
            
            for end in range(start, min(start + 3, len(s))):
                part = s[start: end + 1]
                if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                    continue
                path.append(part)
                backtrack(end + 1, segment + 1, path)
                path.pop()
    
        res = [] 
        path = []
        backtrack(0, 0, path)
        return res

# @lc code=end

