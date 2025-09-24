#
# @lc app=leetcode id=1658 lang=python
# @lcpr version=30203
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # Step 1: Init data
        n = len(nums)
        sum_nums = sum(nums)
        left, right = 0, 0
        # record the sum of window
        window_sum = 0
        # find the longest sum of substring. 
        target = sum_nums - x
        # record the target substring maximum length
        max_len = float('-inf')

        # Step 2: expand window (when find sum of character less than target)
        while right < n:
            window_sum  += nums[right]
            right += 1

            # Step 3: Shrink window (window_sum > target)
            while window_sum > target and left < right:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                max_len = max(max_len, right - left)

        # Step 4 Return the minimum number of operations to reduce 
        return - 1 if max_len == float('-inf') else n - max_len
# @lc code=end



#
# @lcpr case=start
# [1,1,4,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,20,1,1,3]\n10\n
# @lcpr case=end

#

