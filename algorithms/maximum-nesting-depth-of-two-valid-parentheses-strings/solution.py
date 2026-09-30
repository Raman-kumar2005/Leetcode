class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        l=[]
        depth=0
        for i in seq:

            if i =="(":
                depth+=1
                l.append(depth%2)
            else:
                l.append(depth%2)
                depth-=1
        return l