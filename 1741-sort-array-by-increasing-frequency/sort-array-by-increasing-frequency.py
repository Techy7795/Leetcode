class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c=Counter(nums)
        nums.sort(key = lambda x: (c[x],-x))
        return nums