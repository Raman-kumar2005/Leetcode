# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        m=[]
        for i in range(1,len(l)-1):
            if l[i-1]<l[i]>l[i+1]:
                m.append(i)
            elif l[i-1]>l[i]<l[i+1]:
                m.append(i)
        if len(m)<2:
            return [-1,-1]
        
        min_dis=m[1]-m[0]
        for i in range(1,len(m)-1):
            if m[i+1]-m[i]<min_dis:
                min_dis= m[i+1]-m[i]
            

        return [min_dis,m[-1]-m[0]]
