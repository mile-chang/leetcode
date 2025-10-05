#
# @lc app=leetcode id=242 lang=python3
# @lcpr version=30203
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26 # Assuming only lowercase letters a-z

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            # ord -> ASCII value. 'a' = 97, 'b' = 98, ..., 'z' = 122
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#

