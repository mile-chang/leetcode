#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=30202
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[nums[i]] = i
# @lc code=end


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

