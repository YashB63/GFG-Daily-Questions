class Solution:
    def reverseWords(self,str):
        word=[]
        res=[]
        n=len(str)
        for i in range(n-1,-1,-1):
            if str[i]==".":
                
                res.extend(word[::-1])
                res.append(".")
                word=[]
                
            else:
                word.append(str[i])
                
                
        res.extend(word[::-1])
        
        return "".join(res)