#
# @lc app=leetcode id=378 lang=python
# @lcpr version=30202
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # create a flat list of all elements in the matrix
        flat_list = []
        for row in matrix:
            flat_list.extend(row)
        # sort the flat list
        flat_list.sort()
        # return the kth smallest element
        return flat_list[k - 1]
# @lc code=end



#
# @lcpr case=start
# [[1,5,9],[10,11,13],[12,13,15]]\n8\n
# @lcpr case=end

# @lcpr case=start
# [[-5]]\n1\n
# @lcpr case=end

#

