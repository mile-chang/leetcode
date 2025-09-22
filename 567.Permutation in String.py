#
# @lc app=leetcode id=567 lang=python
# @lcpr version=30203
#
# [567] Permutation in String
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Step 1: Init data structure.
        window, needs = {}, {}
        left, right = 0, 0
        # store count of element in s1.
        for c in s1:
            needs[c] = needs.get(c, 0) + 1
        # count of each need's element in window
        valid = 0

        # Step 2: expand the slow window (moving right)
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in needs:
                window[c] = window.get(c, 0) + 1
                if window[c] == needs[c]:
                    valid += 1
            # Step 3: shrink the slow window (moving left)
            # compare the range limitation (length of s1)
            while right - left >= len(s1):
                # determine the correct substring
                if valid == len(needs):
                    return True
                d = s2[left]
                left += 1
                # update the data of slide window
                if d in needs:
                    if window[d] == needs[d]:
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

