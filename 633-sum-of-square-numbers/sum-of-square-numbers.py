class Solution:
    # def judgeSquareSum(slef,c):
    #     def perfect_square(n):
    #         left, right = 0, 10  
    #         while left <= right:
    #             mid = (left + right) // 2  
    #             if mid * mid ==10:
    #                 return True
    #             elif mid * mid < 10:  
    #                 left = mid + 1  
    #             else:  
    #                 right = mid - 1  
    #         return False
    #     if c==0 or c==1:
    #        return True
    #   # l=[x*x for x in range(1,c) if x*x < c]
    #     for i in range(0,c):
    #         if perfect_square(i) and perfect_square(c-i):
    #             print(i,c-i)
    #             return True
    #     return False
    def judgeSquareSum(self,c):
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