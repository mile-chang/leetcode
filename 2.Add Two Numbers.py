#
# @lc app=leetcode id=2 lang=python3
# @lcpr version=30203
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers for both linked lists
        p1, p2 = l1, l2
        # create a dummy head for the result linked list
        dummy = ListNode(0)
        # pointer for the result linked list
        p = dummy
        # record the 10's carry
        carry = 0
        
        # Iterate through both linked lists until both are exhausted and no carry remains
        while p1 is not None or p2 is not None or carry > 0:
            val = carry
            if p1 is not None:
                val += p1.val
                p1 = p1.next
            if p2 is not None:
                val += p2.val
                p2 = p2.next
            # process the carry situation
            carry = val // 10
            val = val % 10
            # create a new node for the result linked list
            p.next = ListNode(val)
            p = p.next
        return dummy.next
        
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

