class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points.sort(key = lambda x: (x[0]**2 + x[1]**2))
        # return points[:k]
        def dist(x,y):
            return x**2 + y**2
        import heapq
        heap=[]
        for x,y in points:
            curr=(-dist(x,y),x,y)
            if len(heap)<k:
                heapq.heappush(heap,curr)
            else:
                heapq.heappushpop(heap,curr)
        return [[x,y] for d,x,y in heap]
        