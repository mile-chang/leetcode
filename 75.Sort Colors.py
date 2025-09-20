#
# @lc app=leetcode id=75 lang=python
# @lcpr version=30203
#
# [75] Sort Colors
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Step 1: create 3 pointers p0, p, p2 to indicate 0, 1, 2
        p0 = 0
        p2 = len(nums) - 1
        p = 0
        # Step 2: swap each num in nums at p0, p, p2
        while p <= p2:
            # 2.1 swap with p0
            if nums[p] == 0:
                self.swap(nums, p0, p)
                p0 += 1
            # 2.2 swap with p2
            elif nums[p] == 2:
                self.swap(nums, p2, p)
                p2 -= 1
            elif nums[p] == 1:
                p += 1
            # 2.3 avoid duplicate swap. (less than p0 is 0)
            if p < p0:
                p = p0
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

