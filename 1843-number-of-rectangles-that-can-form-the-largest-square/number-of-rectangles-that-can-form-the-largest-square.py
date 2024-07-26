class Solution:
    def countGoodRectangles(self, r: List[List[int]]) -> int:
        d={}
        for i in r:
            if min(i) in d:
                d[min(i)]+=1
            else:
                d[min(i)]=1
        return d[max(d)]
        