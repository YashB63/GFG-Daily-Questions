class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        def sL(arr,target):
            l=0
            h = len(arr)-1
            while (l<=h):
                m = (l+h)//2
                if arr[m] == target:
                    l = m+1
                elif arr[m] > target:
                    h = m-1
                else:
                    l = m+1
            return h+1
        arr2.sort()
        ans = []
        for i in arr1:
            ans.append(sL(arr2,i))
        return ans
