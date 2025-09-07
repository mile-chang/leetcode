#
# @lc app=leetcode id=82 lang=python3
# @lcpr version=30202
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create two dummy nodes to handle unique and duplicate values
        dummy_Unique = ListNode(101)
        dummy_Duplicate = ListNode(101)
        # Step 2: Initialize pointers for unique and duplicate lists
        p_Unique, p_Duplicate = dummy_Unique, dummy_Duplicate
        # Step 3: Traverse the original list
        p = head
        while p is not None:
            # Check if the current node is a duplicate.
                # Note: that we also need to check if the current value is the same as the last duplicate value
            if (p.next is not None and p.val == p.next.val) or p.val == p_Duplicate.val:
                p_Duplicate.next = p
                p_Duplicate = p_Duplicate.next
            else:
                p_Unique.next = p
                p_Unique = p_Unique.next
            p = p.next
            # Step 4: Terminate both lists (original and new) to avoid cycles
            p_Unique.next = None
            p_Duplicate.next = None
        return dummy_Unique.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#

