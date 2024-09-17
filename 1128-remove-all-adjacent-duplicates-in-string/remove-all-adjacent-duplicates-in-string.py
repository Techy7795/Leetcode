class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for i in s:
            if not st:
                st.append(i)
            elif st and st[-1]==i:
                st.pop()
                continue
            else:
                st.append(i)
        return ''.join(st)