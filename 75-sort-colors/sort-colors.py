class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=len(a)-1
        while mid <= high:
            if a[mid]==0:
                a[mid],a[low]=a[low],a[mid]
                low+=1
                mid+=1
            elif a[mid]==1:
                mid+=1
            else:
                a[mid],a[high]=a[high],a[mid]
                high-=1
                # mid+=1
        
        