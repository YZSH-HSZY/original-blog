#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#

# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        N = len(buildings)
        res_node = []
        for a,b,c in buildings:
            res_node.append(a)
            res_node.append(b)
            res_node.sort()
# @lc code=end

