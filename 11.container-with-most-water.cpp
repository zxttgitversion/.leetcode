/*
 * @lc app=leetcode id=11 lang=cpp
 *
 * [11] Container With Most Water
 */

// @lc code=start
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int ans = 0;

        while (left < right) {
            int curr_area = min(height[left], height[right]) * (right - left);
            ans = max(curr_area, ans);

            if (height[left] < height[right]) left++;
            else right--;
        }

        return ans;
    }
};
// @lc code=end

