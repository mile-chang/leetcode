#
# @lc app=leetcode id=83 lang=python3
# @lcpr version=30203
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        # use two pointers to remove duplicates in place
        slow, fast = head, head
        while fast is not None:
            if slow.val != fast.val:
                # maintain slow pointer's next to skip duplicates
                slow.next = fast
                slow = slow.next
            # always move the fast pointer
            fast = fast.next
        # important step to avoid cycle in linked list
        slow.next = None
        return head
    
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#

