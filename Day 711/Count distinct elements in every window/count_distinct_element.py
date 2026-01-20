class Solution:
    def countDistinct(self, arr, k):
        dic={}
        l=len(arr)
        ans=[0 for _ in range(l-k+1)]
        le=0
        for i in range(k-1):
            if arr[i] not in dic:
                dic[arr[i]]=1
                le+=1
            else:
                dic[arr[i]]+=1
        for i in range(k-1,l):
            if arr[i] not in dic:
                dic[arr[i]]=1
                le+=1
            else:
                dic[arr[i]]+=1
            pr=i-k+1
            ans[pr]=le
            if dic[arr[pr]]==1:
                dic.pop(arr[pr])
                le-=1
            else:
                dic[arr[pr]]-=1
        return ans