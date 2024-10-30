class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        n=len(arr)
        for i in range(n-1):
            if arr[i]!=0 and arr[i]==arr[i+1]:
                arr[i]=2*arr[i]
                arr[i+1]=0
        ans=[num for num in arr if num!= 0]
        s=len(ans)
        for i in range(s,n):
            ans.append(0)
        return ans