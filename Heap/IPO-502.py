# Example 1:

# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
# Example 2:

# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6

# Time and Space Complexity
# The time complexity of this solution is O(n log n) due to the sorting and heap operations. The space complexity is O(n) for storing the projects and their financials.


from heapq import heappop, heappush, heapify

class Solution:
    def findMaximizedCapital(self, k: int, startingCapital: int, profits: List[int], capital: List[int]) -> int:

        min_heap_by_capital = [(c, p) for c, p in zip(capital, profits)]
        heapify(min_heap_by_capital)
        # print(min_heap_by_capital)
        max_heap_by_profit = []

        while k:
            while min_heap_by_capital and min_heap_by_capital[0][0] <= startingCapital:
                heappush(max_heap_by_profit, -heappop(min_heap_by_capital)[1])
                # print(min_heap_by_capital)

            if not max_heap_by_profit:
                break
           # -ve and -ve = +ve
            startingCapital -= heappop(max_heap_by_profit)
            k -= 1
        return startingCapital
