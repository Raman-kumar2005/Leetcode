class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l=[]
        min_num_arr=[0]*len(nums)
        n=len(nums)
        min_num=nums[-1]
        for i in range(-1,-n-1,-1):
            if nums[i]<min_num:
                min_num=nums[i]
            min_num_arr[i]=min_num
        max_num=nums[0]
        for j in range(n):
            if nums[j]>max_num:
                max_num=nums[j]
            if (max_num-min_num_arr[j])<=k:
                return j
        
        return -1
            