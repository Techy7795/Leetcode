class Solution:
    def countGoodRectangles(self, r: List[List[int]]) -> int:
        l=[min(i) for i in r]
        return l.count(max(l))