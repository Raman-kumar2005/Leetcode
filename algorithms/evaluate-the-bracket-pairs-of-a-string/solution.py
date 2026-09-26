class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        key_value={}
        
        for i in knowledge:
            
            key_value[i[0]]=i[1]
        i=0
        j=0
        new_s=""
        
        while i<len(s):
            
            if s[i] =="(":
                j=i+1
                while j<len(s) and s[j]!=")":
                    j+=1
                key=s[i+1:j]
                new_s+= key_value.get(key,"?")
                i=j+1
            else:
                new_s+=s[i]
                i+=1
        return new_s
