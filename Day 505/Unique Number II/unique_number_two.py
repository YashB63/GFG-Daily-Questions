class Solution:
	def singleNum(self, arr):
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        for i in d:
            if d[i]==1:
                l.append(i)
        return sorted(l)