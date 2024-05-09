#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
            
        return right
# @lc code=end

