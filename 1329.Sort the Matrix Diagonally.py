#
# @lc app=leetcode id=1329 lang=python3
# @lcpr version=30203
#
# [1329] Sort the Matrix Diagonally
#

# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Step 1: get matrix dim
        m, n = len(mat), len(mat[0])
        # Step 2: use dict to collect each diagonal's element.
        diagonals = {} # key : i-j, value: element list
        # Step 3: traverse matrix, group by diagonal
        for i in range(m):
            for j in range(n):
                diagonal_id = i - j # key
                if diagonal_id not in diagonals:
                    diagonals[diagonal_id] = []
                diagonals[diagonal_id].append(mat[i][j])
        # Step 4: sort each diagonal (descending order for pop)
        for diagonal in diagonals.values():
            diagonal.sort(reverse = True)
        # Step 5: fill the sorted element back into matrix
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i-j].pop() 
        return mat
# @lc code=end



#
# @lcpr case=start
# [[3,3,1,1],[2,2,1,2],[1,1,1,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]\n
# @lcpr case=end

#

