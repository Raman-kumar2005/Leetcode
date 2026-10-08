class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        my_list=[]
        stack=[]
        res=""
        for i in  s:
            if i=="(":
                stack.append(i)
                res+=i
            else:
                stack.pop()
                res+=i
            if not stack:
                n=len(res)
                my_list.append(res[1:n-1])
                res=""
            
        return "".join(my_list)
