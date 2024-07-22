class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted([e*e for e in nums])

        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        position = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[position] = nums[left] ** 2
                left += 1
            else:
                result[position] = nums[right] ** 2
                right -= 1
            position -= 1

        return result
