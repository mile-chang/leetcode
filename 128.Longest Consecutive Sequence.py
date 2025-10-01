#
# @lc app=leetcode id=128 lang=python
# @lcpr version=30203
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if it's the start of a sequence
            if n - 1 not in numSet:
                length = 0
                # count the length of the sequence
                while n + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        
# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#

