class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        # Sort the input array nums
        nums.sort()
        
        # Iterate through the array to find quadruplets
        for i in range(n):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n):
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two pointers approach
                k = j + 1
                l = n - 1
                
                while k < l:
                    sum_val = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if sum_val == target:
                        # Found a quadruplet that sums up to target
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        
                        # Skip duplicates for k and l
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif sum_val < target:
                        k += 1
                    else:
                        l -= 1
        
        return ans

        