class Solution:
    def maxDepth(self, s: str) -> int:
        depth_list=[0]
        
        count=0
        for i in s:
            if i=="(":
                count+=1
                depth_list.append(count)
            elif i==")":
                count-=1
                depth_list.append(count)
        return max(depth_list)
