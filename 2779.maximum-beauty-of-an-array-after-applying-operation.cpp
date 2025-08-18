/*
 * @lc app=leetcode id=2779 lang=cpp
 *
 * [2779] Maximum Beauty of an Array After Applying Operation
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int maxBeauty = 0;
        int l = 0, r = 0;

        for (;r < nums.size(); r++) {
            while (nums[r] - nums[l] > 2 * k) {
                l++;
            }
            maxBeauty = max(maxBeauty, r - l + 2);
        }
        return maxBeauty;
        
    }
};
// @lc code=end

