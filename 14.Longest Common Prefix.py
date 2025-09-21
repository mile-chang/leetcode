#
# @lc app=leetcode id=14 lang=python
# @lcpr version=30203
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # m : number of strings.
        # n : number of first string.
        m = len(strs)
        n = len(strs[0])

        for col in range(n):
            # compare all strings at current column
            for row in range(1, m):
                curStr, preStr = strs[row], strs[row - 1]
                # compare each character
                if col >= len(curStr) or col >= len(preStr) or curStr[col] != preStr[col]:
                    return strs[row][:col]
        # all match
        return strs[0]


# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#

