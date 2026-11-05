class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num=max(nums)
        ans=0
        for i in nums:
            ans+=(max_num-i)
        return ans