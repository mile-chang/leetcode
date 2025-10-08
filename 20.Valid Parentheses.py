#
# @lc app=leetcode id=20 lang=python
# @lcpr version=30203
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}
        
        # Stack to keep track of opening brackets
        for c in s:
            if c in closeToOpen:
                # Stack [-1] is the top element of the stack
                # example: "([)]" -> stack = ['(', '['] -> stack[-1] = '['
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#

