class Solution:
    def findMajority(self, arr):
        dici={}
        n=len(arr)
        pst=[]
        for i in arr:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        for key, value in  dici.items():
            if value>len(arr)//3:
                pst.append(key)
        return sorted(pst)