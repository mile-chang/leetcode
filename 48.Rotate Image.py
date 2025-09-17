#
# @lc app=leetcode id=48 lang=python
# @lcpr version=30203
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Step 1: matrix transposition
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Step 2: step by step row reverse
        for row in matrix:
            self.reverse(row)

    def reverse(self, arr):
        i, j = 0, len(arr) - 1
        while j > i:
            # swap (arr[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

