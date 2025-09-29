#
# @lc app=leetcode id=918 lang=python3
# @lcpr version=30203
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # To handle all-negative arrays situation
        globMax, globMin = nums[0], nums[0]

        curMax, curMin = 0, 0
        
        # Sum of entire array
        total = 0

        for num in nums:
            # Case 1: standard Kadane's
            curMax = max(curMax + num, num) 
            # Case 2: find minimun subarray for circular case
            curMin = min(curMin + num, num)
            total += num

            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)
        # Compare to cases
            # Case 1: Non-circular max (globMax)
            # Case 2: Circular max (total - globMin)
        return max(globMax, total - globMin) if globMax > 0 else globMax

# @lc code=end



#
# @lcpr case=start
# [1,-2,3,-2]\n
# @lcpr case=end

# @lcpr case=start
# [5,-3,5]\n
# @lcpr case=end

# @lcpr case=start
# [-3,-2,-3]\n
# @lcpr case=end

#

