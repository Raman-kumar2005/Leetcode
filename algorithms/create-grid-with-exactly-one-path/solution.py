class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res1="."
        res2="."

        output=[]
        for i in range(n-1):
            res1+="#"
            res2+="."
        for i in range(m-1):
            output.append(res1)
        
        output.append(res2)
        return output
        

