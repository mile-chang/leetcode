#
# @lc app=leetcode id=61 lang=python
# @lcpr version=30203
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Step 1: if not head or not head.next or k == 0:
        if head is None or head.next is None or k == 0:
            return head
        # Step 2: calculate the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        # Step 3: process efficient k
        k = k % length
        # Step 4: create a circular list
        tail.next = head
        # Step 5: find the new tail and new head
        steps_to_new_tail = length - k
        while steps_to_new_tail > 0:
            tail = tail.next
            steps_to_new_tail -= 1
        # Step 6: break the circle
        new_head = tail.next
        tail.next = None
        return new_head
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#

