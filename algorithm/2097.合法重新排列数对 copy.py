#
# @lc app=leetcode.cn id=2097 lang=python3
#
# [2097] 合法重新排列数对
#

# @lc code=start
class Solution:
    # def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
    def validArrangement(self, pairs):
        '''
        1. 构建图（pairs[i][0]指向父node，[1]指向子node）
        2. 搜索图（深度搜索，查找一条直接遍历所有节点路径）
        O(n):构建图节点N，预处理节点N，构建图，查找首搜索点2N，搜索标志N，dfs
        '''
        N = len(pairs)
        # 以数组index做唯一node标记（len：10**5）
        # 二维图超限

        class Node():
            def __init__(self, i) -> None:
                self.f_node = []
                self.c_node = []
                self.value = i
        nodes_list = [Node(i) for i in range(N)]
        # 扫描直接填入node父子，len(pairs)**2,time out
        # 借助类哈希避免碰撞思想，填入node父子
        # 10**9 == 2**10**3
        a = 1
        # a bit_num 21位1
        while a < 2**20:
            a = (a << 1) + 1
        # 存放查找字典,{mod_value:[[pairs_node_index,p]]}
        node_find_dict = {}
        # node_find_dict.setdefault(mod,)
        for i in range(N):
            temp0 = node_find_dict.setdefault(pairs[i][0] & a, [])
            temp0.append([i, 0])
            temp1 = node_find_dict.setdefault(pairs[i][1] & a, [])
            temp1.append([i, 1])
        # 父节点
        first_node = None
        # first_node_sign = [False for _ in range(N)]
        maybe_first_node = []
        maybe_last_node = []
        for i in range(N):
            find_list = node_find_dict[pairs[i][0] & a]
            find_list_1 = node_find_dict[pairs[i][1] & a]
            # 处理父节点
            for j in range(len(find_list)):
                if find_list[j][1] == 1 and nodes_list[find_list[j][0]] not in nodes_list[i].f_node:
                    nodes_list[i].f_node.append(nodes_list[find_list[j][0]])
            # 处理子节点
            for j in range(len(find_list_1)):
                if find_list_1[j][1] == 0 and nodes_list[find_list_1[j][0]] not in nodes_list[i].c_node:
                    nodes_list[i].c_node.append(nodes_list[find_list_1[j][0]])
                    # first_node_sign[find_list_1[j][0]] = True
            if not nodes_list[i].f_node:
                first_node = nodes_list[i]
            if len(nodes_list[i].c_node) > len(nodes_list[i].f_node):
                maybe_first_node.append(nodes_list[i])
            else:
                maybe_last_node.append(nodes_list[i])
        # for i in range(N):
        #     if not first_node_sign[i]:
        #         first_node = nodes_list[i]
        #         break
        node_search_sign = [False for _ in range(len(nodes_list))]
        node_path = []

        # 输出
        # def print_node():
        # print(node_path)
        # return 1
        # 深度搜索

        def dfs(n: Node):
            for node in n.c_node:
                if not node_search_sign[node.value]:
                    node_search_sign[node.value] = True
                    node_path.append(pairs[node.value])
                    if dfs(node):
                        return 1
                    else:
                        node_search_sign[node.value] = False
                        node_path.pop()
                # 存在后续节点未访问
                # elif not all([node_search_sign[n_node.value] for n_node in node.c_node]):
                #     if dfs(node):
                #         return 1
                    # else:
                        
            if all(node_search_sign):
                return 1
            return 0
        # [1,2],[2,3],[3,1],[1,4]
        # 0     1       2      3
        # 0->1->2->3
        #        ->0
        # def dfs(n: Node):
        #     if all([True if node_search_sign[_.value] else False for _ in n.c_node]):
        #         node_path.append(pairs[n.value])
        #     else:
        #         for i in n.c_node:
        #             if not node_search_sign[i.value]:
        #                 dfs(i)
                
        if not first_node:
            # first_node = nodes_list[0]
            first_node = maybe_first_node[0]
            # for i in maybe_first_node:
            #     if len(i.c_node) - len(i.f_node) == 1:
            #         first_node = i
            #         break
        first_node = nodes_list[0]
        node_search_sign[first_node.value] = True
        node_path.append(pairs[first_node.value])
        dfs(first_node)
        return node_path
        # print('this node path')
        # print(node_path)
        # @lc code=end

# sorted([len(i.c_node) - len(i.f_node) for i in maybe_first_node])
if __name__ == '__main__':
#     Solution().validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]])
    # oi=[[229,699],[489,928],[92,398],[457,398],[798,838],[75,547],[856,141],[838,141],[356,578],[819,537],[229,458],[229,838],[473,175],[545,826],[705,75],[132,262],[92,974],[141,547],[856,92],[229,856],[838,826],[798,15],[892,157],[578,229],[458,905],[141,856],[157,458],[157,489],[92,458],[838,699],[905,458],[547,798],[928,157],[974,15],[545,132],[545,15],[141,132],[458,175],[856,586],[175,705],[547,229],[928,771],[157,671],[175,473],[132,229],[838,671],[458,356],[262,838],[75,262],[92,798],[156,671],[356,124],[547,175],[262,457],[705,545],[671,156],[928,671],[578,892],[483,856],[586,141],[141,838],[974,928],[356,157],[398,586],[15,157],[905,175],[856,157],[157,856],[398,771],[892,586],[974,473],[262,458],[175,141],[458,92],[175,856],[905,974],[928,229],[826,699],[826,483],[826,905],[905,838],[928,356],[974,905],[124,356],[124,537],[771,545],[262,771],[157,928],[229,157],[547,141],[928,75],[262,974],[856,798],[92,132],[15,141],[141,819],[458,15],[141,905],[458,928],[537,586],[92,819],[473,262],[578,473],[141,458],[15,856],[132,798],[537,974],[586,398],[928,141],[141,262],[771,141],[458,974],[157,771],[398,175],[838,974],[826,92],[175,892],[974,157],[838,356],[699,229],[356,489],[15,771],[771,905],[586,92],[771,92],[798,826],[92,537],[699,458],[671,928],[771,928],[398,928],[699,157],[458,157],[537,905],[974,578],[671,92],[671,75],[157,75],[156,838],[473,398],[928,705],[15,458],[705,458],[157,15],[819,124],[157,92],[699,928],[905,699],[798,262],[458,547],[586,856],[974,489],[856,545],[75,974],[75,578],[905,826],[856,705],[489,547]]
    # oi = [[1,2],[2,3],[3,4],[4,2],[3,5]]
    test_list = [
        [[229,699],[489,928],[92,398],[457,398],[798,838],[75,547],[856,141],[838,141],[356,578],[819,537],[229,458],[229,838],[473,175],[545,826],[705,75],[132,262],[92,974],[141,547],[856,92],[229,856],[838,826],[798,15],[892,157],[578,229],[458,905],[141,856],[157,458],[157,489],[92,458],[838,699],[905,458],[547,798],[928,157],[974,15],[545,132],[545,15],[141,132],[458,175],[856,586],[175,705],[547,229],[928,771],[157,671],[175,473],[132,229],[838,671],[458,356],[262,838],[75,262],[92,798],[156,671],[356,124],[547,175],[262,457],[705,545],[671,156],[928,671],[578,892],[483,856],[586,141],[141,838],[974,928],[356,157],[398,586],[15,157],[905,175],[856,157],[157,856],[398,771],[892,586],[974,473],[262,458],[175,141],[458,92],[175,856],[905,974],[928,229],[826,699],[826,483],[826,905],[905,838],[928,356],[974,905],[124,356],[124,537],[771,545],[262,771],[157,928],[229,157],[547,141],[928,75],[262,974],[856,798],[92,132],[15,141],[141,819],[458,15],[141,905],[458,928],[537,586],[92,819],[473,262],[578,473],[141,458],[15,856],[132,798],[537,974],[586,398],[928,141],[141,262],[771,141],[458,974],[157,771],[398,175],[838,974],[826,92],[175,892],[974,157],[838,356],[699,229],[356,489],[15,771],[771,905],[586,92],[771,92],[798,826],[92,537],[699,458],[671,928],[771,928],[398,928],[699,157],[458,157],[537,905],[974,578],[671,92],[671,75],[157,75],[156,838],[473,398],[928,705],[15,458],[705,458],[157,15],[819,124],[157,92],[699,928],[905,699],[798,262],[458,547],[586,856],[974,489],[856,545],[75,974],[75,578],[905,826],[856,705],[489,547]],
        [[1,2],[2,3],[3,1],[1,4]],
    ]
    for oi in test_list:
        res=Solution().validArrangement(oi)
        print(res)