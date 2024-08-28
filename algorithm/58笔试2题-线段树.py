# import collections
List = list
class Solution:
    def maximumScore(self , nums: List[int], k: int) -> int:
        # write code here
        
        # res_count = collections.defaultdict(0)
        class Node():
            def __init__(self,l,r) -> None:
                self.l = l
                self.r = r
                if l == r:
                    self.l_node = None
                    self.r_node = None
                else:
                    self.l_node = Node(l,(l+r)>>1)
                    self.r_node = Node(((l+r)>>1) + 1,r)
                self.max_value = 0
            def update(self,start,end):
                if start>self.r or end<self.l:
                    return
                if self.l == self.r:
                    self.max_value += 1
                mid = (self.l+self.r)>>1
                # 区间与左区间有交点
                if self.l_node and start<=mid:
                    self.l_node.update(max(self.l,start),min(mid,end))
                # 区间与右区间有交点
                if self.r_node and end>=mid+1:
                    self.r_node.update(max(start,mid+1),min(end,self.r))
                # 更新最大值
                self.max_value = max(self.l_node.max_value if self.l_node else 0,self.r_node.max_value if self.r_node else 0,self.max_value)
            def __str__(self) -> str:
                print('l==%r,r==%r,max==%r' % (self.l,self.r,self.max_value))
                # while self.l_node or self.r_node:
                if self.l_node:
                    print(self.l_node)
                if self.r_node:
                    print(self.r_node)
                return ''
        # root = Node(-10**5,2*10**5)
        root = Node(min(nums)-k,max(nums)+k)
        for i in nums:
            # 更新nums[i]区间
            root.update(i-k,i+k)
            # res_count[j] += 1
            # i-k,i+k
        # max_value = 0
        # for l in res_count:
        #     max_value = max(res_count[l],max_value)
        # print(root)
        return root.max_value

if __name__ == '__main__':
    test_examples = [
        [[4,6,1,2],2],
        [[1,2,3,4],4],
    ]
    for a,b in test_examples:
        print(Solution().maximumScore(a,b))