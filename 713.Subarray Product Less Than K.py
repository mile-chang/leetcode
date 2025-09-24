#
# @lc app=leetcode id=713 lang=python
# @lcpr version=30203
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Init data
        left, right = 0, 0
        # Product of all elements in current window (*)
        windowProduct = 1
        # count for valid subarray.
        count = 0

        # Step 2: expand window
        while right < len(nums):
            windowProduct *= nums[right]
            right += 1

            # Step 3: Shrink window
            while left < right and windowProduct >= k:
                windowProduct //= nums[left]
                left += 1
            # Step 4: Count valid subarrays ending at current right boundary
            # ex: window [a, b, c] has subarrys ending at c : [c], [b, c], [a, b, c]
            count += right - left
        return count 
        
# @lc code=end



#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

