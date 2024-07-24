class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        cycle_length=(n-1)*2
        e_time=time%cycle_length

        if e_time < n:
            return 1+e_time
        else:
            return n-(e_time-(n-1))

