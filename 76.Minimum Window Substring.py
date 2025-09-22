#
# @lc app=leetcode id=76 lang=python3
# @lcpr version=30203
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Step 1: Init data structure and pointers.
        need, window = {}, {}
        # store the count of each element's in t 
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        # define the sliding window border
        left, right = 0, 0
        # count need's element in the window.
        valid = 0
        # store starting index of the minimun substring. 
        start = 0
        length = float('inf')
        
        # Step 2: Expand the window (moving right pointer).
        while right < len(s):
            # c is the character being added to the window.
            c = s[right]
            # expand the window
            right += 1
            # update the widow dict
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
        
            # Step 3: Check window is valid, then shrink it.
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                # if d is the need character, then remove from the window
                d = s[left]
                # shrink the window
                left += 1
                # update the widow dict
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        # Step 4 : return the minimun covering substring
        return "" if length == float('inf') else s[start: start + length]


# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

