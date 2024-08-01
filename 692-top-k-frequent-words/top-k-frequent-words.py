class Solution:
    def topKFrequent(self, nums: List[str], k: int) -> List[str]:
        from collections import Counter
        nums.sort()
        counter=Counter(nums)
        # res=dict(counter)
        # return list(res.keys())[:k]
        return [i[0] for i in counter.most_common(k)]
        