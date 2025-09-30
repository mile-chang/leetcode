#
# @lc app=leetcode id=49 lang=python
# @lcpr version=30203
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # mapping charCount to list of Anagrams
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a to z
            
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            res[key].append(s)
        return res.values()

# @lc code=end



#
# @lcpr case=start
# ["eat","tea","tan","ate","nat","bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

