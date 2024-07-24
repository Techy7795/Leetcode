class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # mapped_nums={}
        # res=[]
        # z=""
        # for i in mapping:
        #     z+=str(i)
        # for i in nums:
        #     s=str(i)
        #     trans=str.maketrans("0123456789",z)
        #     c=int(s.translate(trans))
        #     if c not in mapped_nums:
        #         mapped_nums[c]=[i]
        #     else:
        #         mapped_nums[c].append(i)
        # # print(mapped_nums)
        # for i in sorted(mapped_nums):
        #     for j in mapped_nums[i]:
        #         res.append(j)
        # return res
        trans_rule = str.maketrans({str(i):str(x) for i,x in enumerate(mapping)})
        return sorted(nums, key=lambda x: int(str(x).translate(trans_rule)))