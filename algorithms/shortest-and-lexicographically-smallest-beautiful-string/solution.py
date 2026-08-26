class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l=[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                l.append(s[i:j+1])
        beautiful_sub=[]
        for i in l:
            if i.count("1")==k:
                beautiful_sub.append(i)
        if not beautiful_sub:
            return ""
        min_len = min(len(x) for x in beautiful_sub)
        shortest_subs = [x for x in beautiful_sub if len(x) == min_len]
        return min(shortest_subs)
       
        


        