#
# @lc app=leetcode id=155 lang=python
# @lcpr version=30203
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        # create two stacks
        self.stk = []
        # min_stk always keeps the minimum value at the top
        self.min_stk = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stk.append(val)
        
        if not self.min_stk or val <= self.min_stk[-1]:
            self.min_stk.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        # pop from both stacks if the popped value is the minimum
        if self.min_stk[-1] == self.stk[-1]:
            self.min_stk.pop()

        self.stk.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end



