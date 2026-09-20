class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n=len(intervals)
        intervals.sort()
        total_pair=n*(n-1)//2
        start=[]
        end=[]
        for i in range(n):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        end.sort()
        non_overlapping=0
        end_ind=0
        for j in start:
            while end_ind<n and end[end_ind]<j  :
                end_ind+=1
                
            non_overlapping+=end_ind       
        return total_pair-non_overlapping