/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */

// @lc code=start

#include<vector>
using namespace std;
#include <algorithm>


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        int n = nums.size();

        for (int i = 0; i < n - 2; i++) {
            int x = nums[i];
            if (i > 0 && x == nums[i - 1]) continue;

            int left = i + 1, right = n - 1;

            while (left < right) {
                int s = x + nums[left] + nums[right];
                if (s > 0) {
                    right--;
                } else if (s < 0) {
                    left++;
                } else {
                    ans.push_back({x, nums[left], nums[right]});
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                }
            }

        }
        return ans;
    }
};
// @lc code=end

