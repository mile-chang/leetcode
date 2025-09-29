#
# @lc app=leetcode id=53 lang=python3
# @lcpr version=30203
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Because nums[i] may be nagtive
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            # Check is negtive or not
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum
        
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

