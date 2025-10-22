#
# @lc app=leetcode id=21 lang=python3
# @lcpr version=30203
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        # use a pointer to build the new list
        p = dummy
        p1, p2 = list1, list2
        # compare p1 and p2, and append the smaller one to the new list
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            # p pointer still moves forward
            p = p.next
        # if one of the lists is not empty, append the rest of it to the new list
        p.next = p1 if p1 else p2
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

