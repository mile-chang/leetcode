#
# @lc app=leetcode id=54 lang=python3
# @lcpr version=30203
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        column = len(matrix[0])
        # Step 1: create each bound (top, down, right, left)
        top_bound, down_bound = 0, row - 1
        left_bound, right_bound = 0, column - 1
        # Step 2: create res -> list, if len(res) < matrix nums, do it
        res = []
        while len(res) < row * column:
            # 1. Top side, store left to right strings.
            if top_bound <= down_bound:
                for i in range(left_bound, right_bound + 1):
                    res.append(matrix[top_bound][i])
                top_bound += 1
            # 2. Right side, store top to down strings.
            if left_bound <= right_bound:
                for i in range(top_bound, down_bound + 1):
                    res.append(matrix[i][right_bound])
                right_bound -= 1
            # 3. Down side, store right to left strings.
            if top_bound <= down_bound:
                for i in range(right_bound, left_bound -1, -1):
                    res.append(matrix[down_bound][i])
                down_bound -= 1
            # 4. Left side, store down to up strings.
            if left_bound <= right_bound:
                for i in range(down_bound, top_bound - 1, -1):
                    res.append(matrix[i][left_bound])
                left_bound += 1
        return res
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

