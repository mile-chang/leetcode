#
# @lc app=leetcode id=150 lang=python
# @lcpr version=30203
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for tk in tokens:
            if tk in "+-*/":
                second = stk.pop()
                first = stk.pop()
                if tk == "+":
                    res = first + second
                elif tk == "-":
                    res = first - second
                elif tk == "*":
                    res = first * second
                elif tk == "/":
                    res = int(float(first) / second)  # to truncate toward zero
                stk.append(res)
            else:
                stk.append(int(tk))
        return stk[0]

                
# @lc code=end



#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#

