#
# @lc app=leetcode id=739 lang=python
# @lcpr version=30203
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stk = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                stkT, stkInd = stk.pop()
                res[stkInd] = i - stkInd # update result
            stk.append((t, i)) # push current temp and index to stack
        return res        
# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#

