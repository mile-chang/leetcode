#
# @lc app=leetcode id=11 lang=python3
# @lcpr version=30203
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            res = max(res, area)

            # Move the shorter line's pointer (may be find a taller line)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
            # if height[right] < height[left]:
            #     right -= 1
            # else:
            #     left += 1
        return res
# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

