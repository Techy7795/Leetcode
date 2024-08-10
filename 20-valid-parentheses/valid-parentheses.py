class Solution:
    def isValid(self, s):
        matching_parentheses = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening parentheses
        stack = []

        for char in s:
            if char in matching_parentheses.values():
                # If it's an opening bracket, push to stack
                stack.append(char)
            elif char in matching_parentheses.keys():
                # If it's a closing bracket, check for matching opening bracket
                if not stack or stack[-1] != matching_parentheses[char]:
                    return False
                # Pop the matched opening bracket
                stack.pop()

        # If the stack is empty, all parentheses were matched
        return len(stack) == 0
        # if len(s)%2!=0:
        #     return False
        # op='{[('
        # cl='}])'
        # stack=[]
        # flag=0
        # for i in s:
        #     if i in op:
        #         stack.append(i)
        #     elif i in cl:
        #         x=stack.pop()
        #         print(x,op[cl.index(i)])
        #         flag=1 if (x==op[cl.index(i)]) else 0
        #         if not flag:
        #             return flag
        # return flag


    