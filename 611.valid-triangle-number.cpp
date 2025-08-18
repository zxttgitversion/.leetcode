/*
 * @lc app=leetcode id=611 lang=cpp
 *
 * [611] Valid Triangle Number
 */

// @lc code=start
// 2, 2, 3, 4, 4
// 1, 2, 3, 4, 5
// 245 345

#include <iostream>
#include <vector>
#include <algorithm>
class Solution {
    public:
        int triangleNumber(vector<int>& nums) {
            sort(nums.begin(), nums.end());

            int n = nums.size();
            int cnt = 0;
            // i < j < k
            for (int k = n - 1; k >= 2; k--) {
                int i = 0, j = k - 1;
                while (i < j) {
                    if (nums[i] + nums[j] > nums[k]) {
                        cnt += (j - i); // 所有 i ~ j-1 都能与 j 组成合法三角形
                        j--;
                    } else {
                        i++;
                    }
                }
            }

            return cnt;
        }
    };
    
// @lc code=end

