/*
 * @lc app=leetcode id=2958 lang=cpp
 *
 * [2958] Length of Longest Subarray With at Most K Frequency
 */

// @lc code=start
#include<vector>
#include<iostream>
#include<algorithm>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int max_len = 0;
        int left = 0, right = 0;
        unordered_map<int, int> freq; 

        for (right = 0; right < nums.size(); right++) {
            freq[nums[right]]++;
            while (freq[nums[right]] > k) {
                freq[nums[left]]--;
                left++;
            }
            max_len = max(max_len, right - left + 1);
        }
        return max_len;

    }
};
// @lc code=end

