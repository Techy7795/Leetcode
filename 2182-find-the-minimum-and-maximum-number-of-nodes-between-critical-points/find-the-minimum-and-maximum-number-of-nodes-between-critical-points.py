# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def criticalpoints(l):
            index=[]
            for i in range(1,len(l)-1):
                if (l[i]<l[i-1] and l[i]<l[i+1]) or (l[i]>l[i-1] and l[i]>l[i+1]):
                    index.append(i)
            return index
        l=[]
        while head!=None:
            l.append(head.val)
            head=head.next
        if len(l)==2:
            return [-1,-1]
        index=criticalpoints(l)
        if len(index)==0 or len(index)==1:
            return [-1,-1]
        else:
            print(index)
            maxi=index[-1]-index[0]
            mini=10**5
            for i in range(0,len(index)-1):
                dif=abs(index[i]-index[i+1])
                print(dif)
                mini=min(dif,mini)
            return [mini,maxi]

        



        