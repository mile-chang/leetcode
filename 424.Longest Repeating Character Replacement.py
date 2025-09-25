#
# @lc app=leetcode id=424 lang=python
# @lcpr version=30203
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Step 1: Init
        left, right = 0, 0
        # store the count of character in substring. 
        window = {}
        # max count of x character in window.
        windowMaxCount = 0
        # longest valid substring's length
        length = 0

        # Step 2: expand window
        while right < len(s):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            windowMaxCount = max(windowMaxCount, window[c])
            right += 1

            # Step 3: shrink window
            while left < right and (right - left) - windowMaxCount > k:
                d = s[left]
                left += 1
                window[d] -= 1
            length = max(length, right - left)
        return length
        
# @lc code=end



#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

#

