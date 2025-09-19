#
# @lc app=leetcode id=125 lang=python
# @lcpr version=30203
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Step 1: convert all character to lowercase and filter the space and so on...
        s_lowercase = []
        for c in s:
            # check alphanumeric characters
            if c.isalnum():
                s_lowercase.append(c.lower())
        # Step 2: determining palindrome
        new_string = ''.join(s_lowercase)
        # two pointers, left and right, move toward each other
        left, right = 0, len(new_string) - 1
        while left < right:
            if new_string[left] != new_string[right]:
                return False
            left += 1
            right -= 1
        return True
        
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

