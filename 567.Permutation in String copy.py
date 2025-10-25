#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=30203
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Step 1: Create need and window dict to store character counts
        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        right, left = 0, 0
        valid = 0
        # Step 2: Expand the window with right pointer
        while right < len(s2):
            c = s2[right]
            right += 1
            # Update window counts and valid count
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            # Step 3: Shrink the window when its size matches s1's length
            while right - left >= len(s1):
                # Check if all characters match
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                # Update window counts and valid count
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
# @lc code=end



#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#

