/*
 * @lc app=leetcode id=713 lang=cpp
 *
 * [713] Subarray Product Less Than K
 */

// @lc code=start
#include<vector>
#include<iostream>
#include<numeric>
using namespace std;



class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int cnt = 0;
        int left = 0, right = 0;
        int product = 1;

        for (right = 0; right < nums.size(); right++) {
            product *= nums[right];

            while (product >= k) {
                product /= nums[left];

                left++;
            }
            cnt += (right - left + 1);
        }
        return cnt;
    }
};
// @lc code=end

