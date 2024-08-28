#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
# List = list
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
         欧拉通路问题--图的边全部访问且只访问一次
         dfs时需删除已访问的边，避免死循环，在回溯时添加

         本题起始点已确定，并且保证存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。因此可直接使用欧拉通路算法
        '''
        N = len(tickets)
        import collections
        edges = collections.defaultdict(list)
        for a, b in tickets:
            edges[a].append(b)
        # edges['JFK']
        res = []
        def dfs(node:str):
            while edges[node]:
                edges[node] = sorted(edges[node],reverse=True)
                temp = edges[node].pop()
                dfs(temp)
                res.append(temp)
        dfs('JFK')
        res.append('JFK')
        return res[::-1]
# @lc code=end
# if __name__ == '__main__':
#     test_examples = [
#         [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],
#         [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],

#     ]
#     for i in test_examples:
#         print(Solution().findItinerary(i))
