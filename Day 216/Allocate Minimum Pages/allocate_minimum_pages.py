class Solution:
    
    def findPages(self,n ,arr ,m):
        def possible(n,arr,m,mid):
            sum=0
            std=1
            for i in range(len(arr)):
                if sum + arr[i] <= mid:
                    sum += arr[i]
                else:
                    std += 1
                    if std > m or arr[i] > mid:
                        return False
                    sum = arr[i]
            return True
            
            
        if m > n:
            return -1
        ans=-1
        s=0
        e=sum(arr)
        while s <= e:
            mid = s + (e - s)//2
            if possible(n,arr,m,mid):
                ans=mid
                e = mid - 1
            else:
                s = mid + 1
                
        
        return ans