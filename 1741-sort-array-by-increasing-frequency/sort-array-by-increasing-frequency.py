class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c=Counter(nums)
        nums.sort(key = lambda x: (c[x],-x))
        return nums
        # l=[]
        # for i in c.keys():
        #     l.append([i,c[i]])
        # res=sorted(l,key=lambda x: x[1])
        # print(res)
        # ures=[]
        # for i in res:
        #     for j in range(i[1]):
        #         ures.append(i[0])
        # return ures