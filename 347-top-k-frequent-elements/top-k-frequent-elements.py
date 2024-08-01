class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter=Counter(nums)
        # res=dict(counter)
        # return list(res.keys())[:k]
        return [i[0] for i in counter.most_common(k)]