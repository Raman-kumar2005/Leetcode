class Solution:
    def minOperations(self, s: str) -> int:
        new_s="".join(sorted(s))
        if s == new_s:
            return 0
        elif len(s)<3:
            return -1
        elif s[0]==new_s[-1] and s.count(s[0])==1 and s.count(s[-1])==1  and s[-1]==new_s[0]:
            return 3
        elif s[0]==new_s[0] or s[-1]==new_s[-1]:
            return 1
        else:
            return 2
        