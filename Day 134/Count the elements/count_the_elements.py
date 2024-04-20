class Solution:
    def countElements(self, a, b, n, query, q):
        
        ans=[]
        count=[0]*(max(b)+1)
        for item in b:
            count[item]+=1
        for i in range(1,len(count)):
            count[i]+=count[i-1]
        for item in query:
            el=a[item]
            if el>(len(count)-1):
                ans.append(count[-1])
            else:
                ans.append(count[el])
        return ans