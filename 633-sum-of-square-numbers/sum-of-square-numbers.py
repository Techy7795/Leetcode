class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            sum_val = i * i + j * j
            if sum_val == c:
               return True
            elif sum_val < c:
               i += 1
            else:
               j -= 1
        return False
        