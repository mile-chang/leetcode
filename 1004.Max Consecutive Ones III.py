#
# @lc app=leetcode id=1004 lang=python
# @lcpr version=30203
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Init
        left, right = 0, 0
        # record the count of 0
        count = 0
        # count of substring 
        len_s = 0

        # Step 2: expand window
        while right < len(nums):
            c = nums[right]
            right +=1
            if c == 0:
                count += 1
            # Step 3: shrink window
            while left < right and count > k:
                d = nums[left]
                left += 1
                if d == 0:
                    count -= 1
            len_s = max(len_s, right - left)
        return len_s
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,0,0,0,1,1,1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
# @lcpr case=end

#

