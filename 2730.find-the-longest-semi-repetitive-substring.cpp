/*
 * @lc app=leetcode id=2730 lang=cpp
 *
 * [2730] Find the Longest Semi-Repetitive Substring
 */

// @lc code=start
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    int longestSemiRepetitiveSubstring(string s) {
        int max_len = 1;
        int left = 0, right = 1;
        int cnt = 0;

        for (; right < s.size(); right++) {
            if (s[right] == s[right - 1]) {
                cnt++;
            }

            while (cnt > 1) {
                if (s[left] == s[left + 1]) {
                    cnt--;
                }
                left++;
            }

            max_len = max(max_len, right - left + 1);
            
        }
        return max_len;
    }
};
// @lc code=end

