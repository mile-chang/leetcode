#
# @lc app=leetcode id=59 lang=python
# @lcpr version=30203
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Step 1: create  n*n matrix (all 0)
        matrix = [[0] * n for _ in range(n)]
        # Step 2: create top, down, left, right each bound
        top_bound, down_bound = 0, n - 1
        left_bound, right_bound = 0, n - 1
        # Step 3: create matrix's number
        num = 1
        # Step 4: store num to matrix
        while num <= n * n:
            # 4.1 Top side, left to right 
            if top_bound <= down_bound:
                for i in range(left_bound, right_bound + 1):
                    matrix [top_bound][i] = num
                    num += 1
                # move top_bound downward
                top_bound += 1
            # 4.2 right side, top to down
            if left_bound <= right_bound:
                for i in range(top_bound, down_bound + 1):
                    matrix[i][right_bound] = num
                    num += 1
                # move right_bound leftward
                right_bound -= 1
            # 4.3 Down side, right to left
            if top_bound <= down_bound:
                for i in range(right_bound, left_bound - 1, -1):
                    matrix[down_bound][i] = num
                    num += 1
                # move down_bound move upward
                down_bound -= 1
            # 4.4 left side, down to top
            if left_bound <= right_bound:
                for i in range(down_bound, top_bound - 1, -1):
                    matrix[i][left_bound] = num
                    num += 1
                # move left_bound rightward
                left_bound += 1
        return matrix



# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

