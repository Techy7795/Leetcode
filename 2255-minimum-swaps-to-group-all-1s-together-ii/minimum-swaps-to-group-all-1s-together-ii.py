class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)

        # If there are no 1's or only one 1, no swaps are needed
        if total_ones <= 1:
            return 0

        # Extend the array to handle circular nature
        extended = nums*2
        max_ones_in_window = 0
        current_ones_in_window = 0

        # Calculate max number of 1's in any window of size total_ones
        for i in range(len(extended)):
            if extended[i] == 1:
                current_ones_in_window += 1
            if i >= total_ones:
                if extended[i - total_ones] == 1:
                    current_ones_in_window -= 1
            if i >= total_ones - 1:
                max_ones_in_window = max(max_ones_in_window, current_ones_in_window)

        # Minimum swaps needed is total_ones minus the maximum number of 1's found in any window
        return total_ones - max_ones_in_window
        # n=len(nums)
        # totalOnes=nums.count(1)
        # if totalOnes == 0 or totalOnes == n:
        #     return 0
        # nums=nums+nums[:totalOnes-1]
        # swaps=totalOnes+1
        # for i in range(n):
        #    swaps=min(swaps,(nums[i:i+3]).count(0))
        # return swaps
