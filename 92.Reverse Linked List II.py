#
# @lc app=leetcode id=92 lang=python3
# @lcpr version=30203
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ''' Interative solution '''
    #     # Step 1: determine traveral position
    #     # 1.1 if left == 1, reverse from head.
    #     if left == 1:
    #         return self.reverseN(head, right)
    #     # 1.2 if left > 1, find the predecessor of left
    #     else:
    #         # find the left's predecessor
    #         pre = head
    #         for i in range(1, left - 1):
    #             pre = pre.next
    #         # reverse the sublist starting from pre.next
    #         pre.next = self.reverseN(pre.next, right - left + 1)
    #         return head
    
    # def reverseN(self, head, n):
    #     # Reverse the first n nodes of the linked list starting from head
    #     if head is None or head.next is None:
    #         return head
    #     # Step 1: reverse the first n nodes
    #     prev, curr, next = None, head, head.next
    #     while n > 0:
    #         curr.next = prev
    #         prev = curr
    #         curr = next
    #         if next:
    #             next = next.next
    #         n -= 1
    #     # Step 2: connect the reversed part with the rest of the list
    #     head.next = curr
    #     # now prev is the new head of the reversed sublist
    #     return prev
        ''' recursive solution '''
        # Step 1: determine traveral position
        # 1.1 if left == 1, reverse from head.
        if left == 1:
            return self.reverseN(head, right)
        # 1.2 if left > 1, find the predecessor of left
        else:
            head.next = self.reverseBetween(head.next, left - 1, right - 1)
            return head
        
    # successor
    successor = None
    # reverse the first n nodes of the linked list starting from head
    def reverseN(self, head, n):
        if n == 1:
            # record the (n+1)th node
            self.successor = head.next
            return head
        # recursively reverse the first n-1 nodes
        last = self.reverseN(head.next, n - 1)
        # make head.next point to head
        head.next.next = head
        # connect with the successor
        head.next = self.successor
        return last
    
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

