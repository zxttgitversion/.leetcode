#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        pass
    def length(self) -> int:
        pass

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def find_peak():
            left, right = 0, mountainArr.length() - 1
            while left < right:
                mid = (left + right) // 2

                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid

            return left
        
        def binary_search(left, right, target, asc = True):
            while left <= right:
                mid = (left + right) // 2
                val = mountainArr.get(mid)

                if val == target:
                    return mid
                if asc:
                    if val < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if val > target:
                        left = mid + 1
                    else:
                        right = mid - 1
                
            return -1
        
        peak = find_peak()

        index = binary_search(0, peak, target, asc=True)
        if index != -1:
            return index
        
        index = binary_search(peak + 1, mountainArr.length() - 1, target, asc=False)
        return index if index != -1 else -1
# @lc code=end

