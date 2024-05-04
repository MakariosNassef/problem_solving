#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_s =len(s)
        len_word=0

        while len_s > 0:
            len_s -=1
            if s[len_s] != " ":
                len_word +=1
            
            elif len_word > 0:
                return len_word
        return len_word


# @lc code=end