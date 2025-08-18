/*
 * @lc app=leetcode id=383 lang=cpp
 *
 * [383] Ransom Note
 */

// @lc code=start
#include<string>
#include<vector>
#include<iostream>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int freq[26];
        for (char c : magazine) {
            freq[c - 'a']++;
        }

        for (char c :  ransomNote) {
            if (freq[c - 'a'] <= 0) {
                return false;
            }
            freq[c - 'a']--;
        }
        return true;
    }
};
// @lc code=end

