class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        quo = time // (n - 1)
        mod = time % (n - 1)

        if quo % 2 != 0:
            return n - mod
        return mod + 1
        
        cycle_length=(n-1)*2
        e_time=time%cycle_length

        if e_time < n:
            return 1+e_time
        else:
            return n-(e_time-(n-1))

