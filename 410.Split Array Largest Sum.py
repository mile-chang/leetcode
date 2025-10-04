#
# @lc app=leetcode id=410 lang=python3
# @lcpr version=30203
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
    # Logically same as 1011
        return self.shipWithinDays(nums, k)
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Binary Search [left, right): find the left boundary
        left, right = max(weights), sum(weights) + 1

        while left < right:
            mid = left + (right - left) // 2
            if self.f(weights, mid) <= days:
                right = mid
            else:
                left = mid + 1
        return left
    
    # Calculate how many days needed with capacity cap
    def f(self, weights, cap):
        days = 1
        current = 0
        for w in weights:
            if current + w > cap:
                days += 1
                current = 0
            current += w
        return days

# @lc code=end



#
# @lcpr case=start
# [7,2,5,10,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

#

