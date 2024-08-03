class Solution:
	def removeDups(self, S):
        a=''
        l=[]
        for i in S:
            if i not in l:
                l.append(i)
        for i in l:
            a+=i
        return a