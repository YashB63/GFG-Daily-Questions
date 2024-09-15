class Solution:
    def sort012(self, arr):
        n=len(arr)
        l,m,h=0,0,n-1
        while m<=h:
            if arr[m]==0:
                arr[l],arr[m]=arr[m],arr[l]
                l+=1
                m+=1
            elif arr[m]==1:
                m+=1
            else:
                arr[m],arr[h]=arr[h],arr[m]
                h-=1
        return arr