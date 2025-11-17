#
# @lc app=leetcode id=287 lang=python3
# @lcpr version=30300
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Tortoise and Hare (Cycle Detection)
        slow = 0
        fast = 0

        # Phase 1: Finding the intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Finding the entrance to the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
# @lc code=end



#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#

