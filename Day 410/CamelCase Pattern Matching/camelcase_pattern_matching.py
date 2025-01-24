class Solution:
    def camelCase(self,arr,pat):
        res=[]
        for word in arr:
            i=0
            j=0
            while i<len(word) and j<len(pat):
                if word[i].islower():
                    i=i+1
                elif word[i]!=pat[j]:
                    break
                else:
                    j=j+1
                    i=i+1
            if j==len(pat):
                res.append(word)
        return res