#
# @lc app=leetcode id=34 lang=python
# @lcpr version=30203
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        res.append(self.left_bound(nums, target))
        res.append(self.right_bound(nums, target))
        return res
    
    def left_bound(self, nums, target):
        # Use [left, right]
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                # shrink right border
                right = mid - 1
            
        # Determine the target exist or not
        if left < 0 or left >= len(nums):
            return -1
        return left if nums[left] == target else -1
    def right_bound(self, nums, target):
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                # shrink left border
                left = mid + 1
            
        # Determine the target exist or not
        if right < 0 or right >= len(nums):
            return -1
        return right if nums[right] == target else -1
    
        
# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

