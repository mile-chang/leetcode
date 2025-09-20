#
# @lc app=leetcode id=977 lang=python3
# @lcpr version=30203
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Step 1: init three pointers
        n = len(nums)
        head, end = 0, n -1
        p = n - 1
        res = [0] * n
        # Step 2: compare head to end
        while head <= end:
            if abs(nums[head]) > abs(nums[end]):
                res[p] = nums[head] ** 2
                head += 1
            else:
                res[p] = nums[end] ** 2
                end -= 1
            p -= 1
        return res
# @lc code=end



#
# @lcpr case=start
# [-4,-1,0,3,10]\n
# @lcpr case=end

# @lcpr case=start
# [-7,-3,2,3,11]\n
# @lcpr case=end

#

