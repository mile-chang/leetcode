#
# @lc app=leetcode id=74 lang=python3
# @lcpr version=30203
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # Map the 2D matrix to a 1D array and perform binary search
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if self.get_value(matrix, mid) == target:
                return True
            elif self.get_value(matrix, mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    # Get the value from the 2D matrix using a 1D index
    def get_value(self, matrix, index):
        m = len(matrix)
        n = len(matrix[0])
        # Calculate the row and column from the 1D index
        row = index // n
        col = index % n
        return matrix[row][col]
        
# @lc code=end



#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#

