class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m=str(n)
        l=list(map(int,m))
        digit_sum=0
        digit_product=1
        for i in l:
            digit_sum+=i
            digit_product*=i
        return n%(digit_sum+digit_product)==0