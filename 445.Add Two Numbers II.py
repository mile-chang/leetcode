#
# @lc app=leetcode id=445 lang=python3
# @lcpr version=30203
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = []
        l2_stack = []
        # put the values into stacks
        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next
        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next
        # add the 10's digit carry
        carry = 0
        dummy = ListNode(0)

        # if l1_stack is not empty or l2_stack is not empty or carry > 0
        # create a new node
        while l1_stack or l2_stack or carry > 0:
            value = carry
            if l1_stack:
                value += l1_stack.pop()
            if l2_stack:
                value += l2_stack.pop()
            carry = value // 10
            value = value % 10
            # Most important step:
            #　insert the new node to the front of the linked list
            new_node = ListNode(value)
            new_node.next = dummy.next
            dummy.next = new_node
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [7,2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

#

