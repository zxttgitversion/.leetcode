/*
 * @lc app=leetcode id=2824 lang=cpp
 *
 * [2824] Count Pairs Whose Sum is Less than Target
 */

// @lc code=start


#include <iostream>
#include <vector>
#include <algorithm>
class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        
        sort(nums.begin(), nums.end());

        int left = 0, right = nums.size() - 1;
        int cnt = 0;

        while ((left < right))
        {
            int sum = nums[left] + nums[right];

            if (sum < target) {
                cnt += (right - left);
                left ++;
            } else {
                right--;
            }
        }
        return cnt;
        
    }
};
// @lc code=end

