#
# @lc app=leetcode id=853 lang=python
# @lcpr version=30203
#
# [853] Car Fleet
#

# @lc code=start
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Create pairs of (position, speed) and sort by position in descending order
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            stack.append(float(target - p) / s)  # Calculate time to reach the target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Remove the last time if it's less than or equal to the one before it
        return len(stack)  # Number of fleets
# @lc code=end



#
# @lcpr case=start
# 12\n[10,8,0,5,3]\n[2,4,1,1,3]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[3]\n[3]\n
# @lcpr case=end

# @lcpr case=start
# 100\n[0,2,4]\n[4,2,1]\n
# @lcpr case=end

#

