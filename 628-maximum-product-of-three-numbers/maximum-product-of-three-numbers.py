class Solution:
    def maximumProduct(self,nums: List[int]) -> int:
        first_max = float('-inf')
        second_max = first_max
        third_max = first_max

        first_min = float('inf')
        second_min = first_min

        for i in range(len(nums)):
            if first_max <= nums[i]:
                third_max = second_max
                second_max = first_max
                first_max = nums[i]
            elif second_max <= nums[i]:
                third_max = second_max
                second_max = nums[i]
            elif third_max <= nums[i]:
                third_max = nums[i]

            if(first_min >= nums[i]):
                second_min = first_min
                first_min = nums[i]
            elif second_min >= nums[i]:
                second_min = nums[i]
        
        return max(first_max * second_max * third_max, first_min * second_min * first_max)