class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l=[]
        
        
        for i in nums:
            if i%k==0:
                l.append(i)
        for i in range(k,201,k):
            if i not in l:
                return i