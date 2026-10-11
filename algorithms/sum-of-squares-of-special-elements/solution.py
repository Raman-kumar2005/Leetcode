class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            if n%(i+1)==0:
                count+=nums[i]*nums[i]
        return count
            
        