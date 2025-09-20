#
# @lc app=leetcode id=88 lang=python3
# @lcpr version=30203
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Step 1: init 3 pointers
        i = m - 1
        j = n - 1
        p = len(nums1) - 1
        # Step 2: compare from end to first, then merge each other.
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        # Step 3: process remaining element
        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1
        return nums1
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,0,0,0]\n3\n[2,5,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n[]\n0\n
# @lcpr case=end

# @lcpr case=start
# [0]\n0\n[1]\n1\n
# @lcpr case=end

#

