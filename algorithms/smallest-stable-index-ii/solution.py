class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_num=nums[0]
        
        n=len(nums)
        l=[]
        for i in range(n):
            if nums[i]>max_num:
                max_num=nums[i]
            min_num=min(nums[i:n])

            if max_num-min_num<=k:
                l.append(i)
        if l:
            return min(l)
        return -1