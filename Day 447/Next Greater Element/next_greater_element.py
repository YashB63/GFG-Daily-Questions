class Solution:
    def nextLargerElement(self, arr):
        s=[]
        n=len(arr)
        res=[0 for i in range(n)]
        for i in range(n):
            if len(s)==0:
                s.append(i)
                continue
            while len(s)!=0 and arr[s[-1]]<arr[i] and i>0 :
                k=s.pop()
                res[k]=arr[i]
            s.append(i)
        for i in range(len(res)):
            if res[i]==0:
                res[i]=-1
        return res