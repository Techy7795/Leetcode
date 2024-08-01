class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for s in strs:
            s_sorted=sorted(s)
            key=tuple(s_sorted)
            ans[key].append(s)
        return ans.values()

        ans=defaultdict(list)
        for s in strs:
            key=[0]*26
            for c in s:
                key[ord(c)-ord('a')]+=1
            key=tuple(key)
            ans[key].append(s)
        return ans.values()
            