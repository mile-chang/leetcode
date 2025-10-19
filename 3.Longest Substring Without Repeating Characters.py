#
# @lc app=leetcode id=3 lang=python
# @lcpr version=30203
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        """ Method 1: Using Dictionary for Sliding Window """
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
    
    ''' Method 2: Using Set for Sliding Window '''
    def lengthOfLongestSubstring_set(self, s: str) -> int:
        char_set = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)

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

