#
# @lc app=leetcode id=15 lang=python
# @lcpr version=30203
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # If the number is the same as the one before, skip it to avoid duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            
            # use two pointers to find the other two numbers
            left, right = i + 1, len(nums) - 1

            while left < right:
                if a + nums[left] + nums[right] < 0:
                    left += 1
                elif a + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([a, nums[left], nums[right]])
                    # Move the left pointer to the right, skipping over duplicates
                    left += 1
                    # Unique check for left pointer
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

