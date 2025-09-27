#
# @lc app=leetcode id=220 lang=python
# @lcpr version=30203
#
# [220] Contains Duplicate III
#

# @lc code=start
from sortedcontainers import SortedList
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        # i != j, |i - j| <= indexDiff, |nums[i] - nums[j]| <= valueDiff
        
        window = SortedList()

        for i in range(len(nums)):
            # Step 1: Find the closest element in window.
            pos = window.bisect_left(nums[i])
            # Step 2: Find the element that is slightly larger than nums[i].
            if pos < len(window) and window[pos] - nums[i] <= valueDiff:
                return True
            # Step 3: Find the element that is slightly less than nums[i]
            if pos > 0 and nums[i] - window[pos - 1] <= valueDiff:
                return True 
            
            # Step 4: expand window
            window.add(nums[i])

            if len(window) > indexDiff:
                # Step 5: shrink window
                window.remove(nums[i - indexDiff])

        return False
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,5,9,1,5,9]\n2\n3\n
# @lcpr case=end

#

