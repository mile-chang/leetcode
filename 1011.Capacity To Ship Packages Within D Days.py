#
# @lc app=leetcode id=1011 lang=python3
# @lcpr version=30203
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
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
# [1,2,3,4,5,6,7,8,9,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,4,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,1]\n4\n
# @lcpr case=end

#

