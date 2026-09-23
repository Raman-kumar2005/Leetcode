class Solution {
    public int minOperations(int[] nums, int x) {
        int target_sum=Arrays.stream(nums).sum()-x;
        if (target_sum<0){
            return -1;
        }else if (target_sum==0){
            return nums.length;
        }
        int i= 0;
        int max_len = -1;
        int current_sum=0;
        for (int j= 0; j<nums.length;j++){
            current_sum+=nums[j];
            
            while (current_sum > target_sum && i<=j){
                current_sum-=nums[i];
                i++;
            }
            if (current_sum==target_sum){
                int current_len =j-i+1;
                max_len = Math.max(max_len, current_len);
            }
            
        }
        if (max_len!= -1){
                return  nums.length - max_len;
            }else{
                return -1;
            }
    }
}