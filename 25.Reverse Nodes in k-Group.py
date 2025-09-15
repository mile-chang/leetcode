#
# @lc app=leetcode id=25 lang=python3
# @lcpr version=30203
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        ''' Iterative solution '''
    #     if head is None:
    #         return None
    #     # Step 1:  create a interval [a, b) that contains k nodes
    #     a, b = head, head
    #     # 1.1 if less than k nodes, do not reverse, base case
    #     for i in range(k):
    #         if b is None:
    #             return head
    #         b = b.next
    #     # Step 2: reverse the interval [a, b)
    #     new_head = self.reverseN(a, k)
    #     # Step 3: reversed the subsequent k-group and connect to the first part
    #     a.next = self.reverseKGroup(b, k)
    #     return new_head
    
    # # reverse the linked list in the interval [a, b)
    # def reverseN(self, head, n):
    #     if head is None or head.next is None:
    #         return head
    #     prev, curr, next = None, head, head.next
    #     while n > 0:
    #         curr.next = prev
    #         prev = curr
    #         curr = next
    #         if next:
    #             next = next.next
    #         n -= 1
    #     head.next = curr
    #     return prev
    
        ''' Traverse solution '''
        if head is None:
            return None
        # Step 1: check if there are at least k nodes left in the linked list
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        # 1.1 if less than k nodes, do not reverse, base case
        if count < k:
            return head
        # Step 2: reverse the first k nodes
        new_head = self.reverseN(head, k)
        head.next = self.reverseKGroup(curr, k)
        return new_head

    successor = None
    def reverseN(self, head, n):
        # record the (n+1)th node
        if n == 1:
            self.successor = head.next
            return head
        # recursively reverse the first n-1 nodes
        last = self.reverseN(head.next, n - 1)

        # reverse the current node
        head.next.next = head
        head.next = self.successor
        return last


        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

