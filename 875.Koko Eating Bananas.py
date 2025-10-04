#
# @lc app=leetcode id=875 lang=python
# @lcpr version=30203
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # [left, right): possible eating speeds
        left, right = 1, max(piles) + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.f(piles, mid) <= h:
                right = mid
            elif self.f(piles, mid) > h:
                left = mid + 1
            elif self.f(piles, mid) == h:
                right = mid
        return left
    
    # Definition of f(k): hours needed to eat all bananas at speed k
    # f(k) is a decreasing function
    def f(self, piles, k):
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

