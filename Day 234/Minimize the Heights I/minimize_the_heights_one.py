class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        s, l = arr[0], arr[-1]
        diff = l-s
        
        s += k
        l -= k
        mn, mx = s, l
        for i in range(n-1):
            mn = min(s, arr[i+1]-k)
            mx = max(l, arr[i]+k)
            
            if diff > mx-mn:
                diff = mx-mn
                
        return diff