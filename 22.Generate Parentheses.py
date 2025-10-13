#
# @lc app=leetcode id=22 lang=python
# @lcpr version=30203
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add '(' if open < n
        # only add ')' if close < open
        # valid if open == close == n

        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop() # backtrack

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop() # backtrack
        backtrack(0, 0)
        return res
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

