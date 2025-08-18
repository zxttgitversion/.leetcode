/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
#include<string>
#include<algorithm>
#include<unordered_set>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_len = 0;
        unordered_set<char> window;
        int left = 0; int right = 0;

        while (right < s.length()) {
            char c = s[right];
            if (window.find(c) == window.end()) {
                
                window.insert(c);
                max_len = max(max_len, right - left + 1);
                right++;

            } else {
                window.erase(c);
                left++;
            }

        }
        return max_len;
    }
};
// @lc code=end

