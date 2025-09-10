#
# @lc app=leetcode id=373 lang=python3
# @lcpr version=30203
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
from queue import PriorityQueue
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Store triplets (num1[i], nums2[i], i)
        # i records the index position of the nums2 element, used to generate the next node
        pq = PriorityQueue()
        
        for i in range(len(nums1)):
            # initialize the priority queue with pairs (nums1[i], nums2[0])
            pq.put((nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        
        res = []

        while not pq.empty() and k > 0:
            _, n1, n2, index = pq.get()
            k -= 1
            # put linklist's next node
            next_index = index + 1
            if next_index < len(nums2):
                # tuple: (sum, num1, num2, index in nums2)
                pq.put((n1 + nums2[next_index], n1, nums2[next_index], next_index))
            pair = [n1, n2]
            res.append(pair)
        return res     

# @lc code=end



#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#

