/*
 * @lc app=leetcode id=167 lang=cpp
 *
 * [167] Two Sum II - Input Array Is Sorted
 */

// @lc code=start

#include <iostream>
using namespace std;
#include <vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        while (true)
        {
            int s = numbers[left] + numbers[right];
            if (s == target) {
                return {left + 1, right + 1};
            }
            s > target ? right-- : left++;
        }
        
    }
};
// @lc code=end

