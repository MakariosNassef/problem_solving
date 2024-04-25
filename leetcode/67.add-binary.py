#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # result = bin(int(a,2)+int(b,2))
        # return result[2:]
        result = ""
        carry = 0
        i , j =len(a)-1, len(b)-1
        while i >= 0 or j>=0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result = str(total % 2) + result
            carry = total // 2
        return result
# @lc code=end