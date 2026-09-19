class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        d={}
        for i in digits:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count=0
        for i in range(100,999,2):
            s=str(i)
            a=int(str(i)[0])
            b=int(str(i)[1])
            c=int(str(i)[2])
            if (d.get(a, 0) >= s.count(str(a))) and (d.get(b, 0) >= s.count(str(b))) and (d.get(c, 0) >= s.count(str(c))):
                count+=1
                
        return count
