#
# @lc app=leetcode id=283 lang=python
# @lcpr version=30203
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return 0
        slow = 0
        fast = 0
        # step 1: remove non-zero elements
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        # step 2: fill the rest with 0
        for i in range(slow, len(nums)):
            nums[i] = 0
        return nums
# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

