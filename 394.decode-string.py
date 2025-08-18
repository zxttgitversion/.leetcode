#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        currNum = 0
        currStr = ''

        for c in s:
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            elif c == '[':
                numStack.append(currNum)
                strStack.append(currStr)
                currNum = 0
                currStr = ''
            elif c == ']':
                repeatTimes = numStack.pop()
                prevString = strStack.pop()
                currStr = prevString + currStr * repeatTimes
            else:
                currStr += c

        return currStr
# @lc code=end

