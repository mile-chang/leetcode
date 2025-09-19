#
# @lc app=leetcode id=80 lang=python3
# @lcpr version=30203
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Step 1: use fast, slow to mantain nums[0...slow]
        fast, slow = 0, 0
        # Step 2: count of element's duplicating times
        count = 0
        # Step 3: replace nums
        while fast < len(nums):
            # 3.1 put new element nums[fast] into nums[0..slow].
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            # 3.2 duplicating times less than 2, add it. 
            elif slow < fast and count < 2:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
            count += 1
            # 3.3 fast encounter new different elemnt, reset the duplicate times.
            if fast < len(nums) and nums[fast] != nums[fast - 1]:
                count = 0
        # nums[0...slow]'s length is index + 1
        return slow + 1
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

