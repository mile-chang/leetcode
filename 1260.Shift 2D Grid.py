#
# @lc app=leetcode id=1260 lang=python
# @lcpr version=30203
#
# [1260] Shift 2D Grid
#

# @lc code=start
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Step 1: convert to 1 dimension array
        m, n = len(grid), len(grid[0])
        total = m * n
        # Step 2: avoid duplicate calculate
        k = k % total
        # Step 3: create result grid
        result = [[0] * n for _ in range(m)]
        # Step 4: traverse each element to calculate new location
        for i in range(m):
            for j in range(n):
                # current element
                value = grid[i][j]
                
                # 4.1 convert to 1 dim index
                cur_index = i * n + j
                
                # 4.2 calculate moved new_index
                # avoid out of 1 dim array range.(circular)
                new_index = (cur_index + k) % total

                # 4.3 convert 1 dim array to 2 dim
                # new_i = new_index // n (row)
                # new_j = new_index % n (column)
                new_i, new_j = divmod(new_index, n)
                result[new_i][new_j] = value
        return result

# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n9\n
# @lcpr case=end

#

