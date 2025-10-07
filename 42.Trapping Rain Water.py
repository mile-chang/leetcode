#
# @lc app=leetcode id=42 lang=python
# @lcpr version=30203
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) == 0:
            return 0
        
        n = len(height)
        res = 0

        ''' Use prefix '''
        l_max = [0] * n
        r_max = [0] * n
        # Initialize
        l_max[0] = height[0]
        r_max[n-1] = height[n-1]

        # Left to right to calculate l_max
        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], height[i])
        # Right to left to calculate r_max
        for i in range(n - 2, -1, -1):
            r_max[i] = max(r_max[i + 1], height[i])
        # Calculate the water trapped
        for i in range(n):
            res += min(l_max[i], r_max[i]) - height[i]
        return res
 
# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

