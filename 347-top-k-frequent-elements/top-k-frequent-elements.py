class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter=Counter(nums)
        heap=[]
        for key,val in counter.items():
            if len(heap)<k:
                heapq.heappush(heap,(val,key))
            else:
                heapq.heappushpop(heap,(val,key))
        return [h[1] for h in heap]


        # return [i[0] for i in counter.most_common(k)]
        