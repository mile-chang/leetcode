#
# @lc app=leetcode id=167 lang=python3
# @lcpr version=30202
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use left and right pointers moveing towards each other
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers [right]
            if sum == target:
                return [left + 1, right + 1]
            # if the sum is less than the target, move the left pointer to the right
            elif sum < target:
                left += 1
            # if the sum is greater than the target, move the right pointer to the left
            else:
                right -= 1
        # If no solution is found, though the problem guarantees one, return [-1, -1]
        return [-1, -1]
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#

