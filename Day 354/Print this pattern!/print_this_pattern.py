class Solution:
	def printPattern(self, N):
        l=[N]*N
        L=[]
        for i in range(N):
            L.append(l+l[:-1:][::-1])
            for i in range(i+1,N):
                l[i]-=1
        L.extend(L[:-1:][::-1])
        for i in L:
            for j in i:
                print(j,end="")
            print()