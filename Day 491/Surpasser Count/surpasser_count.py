class Solution:
    def findSurpasser(self, arr):
        n = len(arr)
        ans = [0]*(n)
        m_arr = []
        
        for i in range(n):
            m_arr.append((arr[i],i))
            
        self.mergesort(m_arr,ans,0,n-1)
        return ans
        
    def mergesort(self,arr,ans,l,r):
        if (l<r):
            mid = (l+r)//2
            self.mergesort(arr,ans,l,mid)
            self.mergesort(arr,ans,mid+1,r)
            self.merge(arr,ans,l,mid,r)
            
    def merge(self,arr,ans,l,mid,r):
        temp = []
        
        i=l
        j=mid+1
       
        while i<=mid and j<=r:
            if arr[i][0] < arr[j][0]:
                ans[arr[i][1]] += (r-j+1)
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
               
        while i<=mid:
            temp.append(arr[i])
            i+=1
            
        while j<=r:
            temp.append(arr[j])
            j+=1
            
        k=0
        for i in range(l,r+1):
            arr[i] = temp[k]
            k+=1