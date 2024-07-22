class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([e*e for e in nums])