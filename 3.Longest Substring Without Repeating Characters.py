#
# @lc app=leetcode id=3 lang=python
# @lcpr version=30203
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Initialize sliding window variables.
        window = {}
        left, right = 0, 0
        res = 0

        # Step 2: Expand window by moving right window.
        while right < len(s):
            c = s[right]
            right += 1
            # Add character to window and update count
            window[c] = window.get(c, 0) + 1
            
            # Step 3: Shrink window when duplicate character found.
            while window[c] > 1:
                d = s[left]
                left += 1
                # Remove count of each character from window.
                window[d] -= 1
            # Step 4: Update maximum length (window no duplicate)
            res = max(res, right - left)
        return res       
        
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

