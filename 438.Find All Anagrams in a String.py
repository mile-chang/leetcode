#
# @lc app=leetcode id=438 lang=python3
# @lcpr version=30203
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Step 1: inin data structure.
        window, needs = {}, {}
        left, right = 0, 0
        # store count of each element in p.
        for c in p:
            needs[c] = needs.get(c, 0) + 1
        # the count of each need's elemnet in window,
        valid = 0
        res = []

        # Step 2: expand the slide window (moving right)
        while right < len(s):
            # get the current character
            c = s[right]
            right += 1
            if c in needs:
                window[c] = window.get(c, 0) + 1
                if window[c] == needs[c]:
                    valid +=1
            # Step 3: shrink the slide window (moving left)
            while right - left >= len(p):
                # Step 4: update result.
                if valid == len(needs):
                    res.append(left)
                # moving left
                d = s[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -=1
                    window[d] -= 1
        return res
# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

