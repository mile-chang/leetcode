#
# @lc app=leetcode id=209 lang=python
# @lcpr version=30203
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0 
        
        # Count of length in window
        res = float('inf')
        sum_window = 0

        while right < len(nums):
            sum_window += nums[right]
            # Expand window
            right += 1
            
            while left < right and sum_window >= target:
                res = min(res, right - left)
                sum_window -= nums[left]
                # Shrink window
                left += 1
        return res if res != float('inf') else 0

# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

