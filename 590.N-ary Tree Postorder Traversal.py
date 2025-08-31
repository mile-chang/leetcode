#
# @lc app=leetcode id=590 lang=python3
# @lcpr version=30202
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """ Method 1 """
        # result = []
        # if root is None:
        #     return result
        
        # for child in root.children:
        #     result.extend(self.postorder(child))
        # result.append(root.val)
        # return result
        
        """ Method 2 """
        self.result = []
        self.traverse(root)
        return self.result
    
    def traverse(self, root: 'Node') -> None:
        if root is None:
            return
        for child in root.children:
            self.traverse(child)
        self.result.append(root.val)
        
# @lc code=end



#
# @lcpr case=start
# [1,null,3,2,4,null,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]\n
# @lcpr case=end

#

