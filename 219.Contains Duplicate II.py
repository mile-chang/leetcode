#
# @lc app=leetcode id=219 lang=python3
# @lcpr version=30203
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Conditions: i != j, |i - j| <= k
        # Find two identical numbers whose indices are ≤ k apart.
        
        # Step 1: Init
        left, right = 0, 0
        window = set()
        # Step 2: expand window
        while right < len(nums):
            if nums[right] in window:
                return True
            window.add(nums[right])
            right += 1
            # Step 3: shrink window
            if right - left > k:
                window.remove(nums[left])
                left += 1
        return False
            
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#

