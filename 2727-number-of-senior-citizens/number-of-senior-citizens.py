class Solution:
    def countSeniors(self, d: List[str]) -> int:
        c=0
        for i in d:
            # age=i[11]+i[12]
            if int(i[11:13])>60:
                c+=1
        return c

        