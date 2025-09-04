#
# @lc app=leetcode id=797 lang=python3
# @lcpr version=30202
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.traverse(graph, 0)
        return self.res
    
    def traverse(self, graph, s):
        self.path.append(s)
        # if reach the end
        if s == len(graph) - 1:
            self.res.append(self.path.copy())
            self.path.pop()
            return
        # traverse adjacent nodes
        for v in graph[s]:
            self.traverse(graph, v)
        
        self.path.pop()
# @lc code=end



#
# @lcpr case=start
# [[1,2],[3],[3],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,1],[3,2,4],[3],[4],[]]\n
# @lcpr case=end

#

