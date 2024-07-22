class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        L=[]
        for i in zip(heights,names):
            L.append(list(i))
        return [e[1] for e in sorted(L)[::-1]]
        