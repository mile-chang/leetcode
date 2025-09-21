#
# @lc app=leetcode id=867 lang=python
# @lcpr version=30203
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        # Step 1: create transpose matrix, all zeros
        tra_matrix = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                # add matrix's int in tra_matrix
                tra_matrix[j][i] = matrix[i][j]
        return tra_matrix
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#

