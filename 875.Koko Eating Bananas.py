#
# @lc app=leetcode id=875 lang=python3
# @lcpr version=30203
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Find the minimum eating speed k such that f(k) <= h
        left, right = 1, max(piles) + 1 

        # [left, right): possible eating speeds
        while left < right:
            mid = left + (right - left) // 2
            if self.f(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left
    
    # Definition of f(k): hours needed to eat all bananas at speed k
    # f(k) is a decreasing function
    def f(self, piles: List[int], k: int) -> int:
        hours = 0
        for p in piles:
            hours += p // k
            if p % k != 0:
                hours += 1
        return hours
# @lc code=end



#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#

