#
# @lc app=leetcode id=395 lang=python
# @lcpr version=30203
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # substring's length
        length = 0

        for i in range(1, 27):
            # Only have i distinct characters in the window.
            length = max(length, self.longestKLetterSubstr(s, k, i))
        return length
        
    def longestKLetterSubstr(self, s, k, count):
        # record the result
        res = 0
        left, right = 0, 0
        # Count of each character in window.
        windowCount = [0] * 26
        # Number of character types in window.
        windowUniqueCount = 0
        # Number of valid characters
        windowValidCount = 0

        while right < len(s):
            c = s[right]
            # Add character types
            if windowCount[ord(c) - ord('a')] == 0:
                windowUniqueCount += 1
            windowCount[ord(c) - ord('a')] += 1
            # Add valid character
            if windowCount[ord(c) - ord('a')] == k:
                windowValidCount +=1
            # Expand the window
            right += 1

            # Shrink the window
            while windowUniqueCount > count :
                d = s[left]
                # Reduce valid character
                if windowCount[ord(d) - ord('a')] == k:
                    windowValidCount -= 1
                windowCount[ord(d) - ord('a')] -= 1
                # Reduce character types
                if windowCount[ord(d) - ord('a')] == 0:
                    windowUniqueCount -= 1
                left += 1
            
            # If each count of types character >= k in window, update the result
            if windowValidCount == count:
                res = max(res, right - left)
        return res

# @lc code=end



#
# @lcpr case=start
# "aaabb"\n3\n
# @lcpr case=end

# @lcpr case=start
# "ababbc"\n2\n
# @lcpr case=end

#

