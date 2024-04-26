#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return (str(x) == str(x)[::-1])

        if x < 0:
            return (False)
        s = str(x)
        reverse = s[::-1]
        if s==reverse:
            return (True)
        else:
            return (False)


            
# @lc code=end

