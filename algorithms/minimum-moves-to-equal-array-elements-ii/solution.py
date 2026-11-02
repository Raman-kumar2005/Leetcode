class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_num=min(nums)
        n=len(nums)
        
        return sum((num-min_num) for num in nums)
