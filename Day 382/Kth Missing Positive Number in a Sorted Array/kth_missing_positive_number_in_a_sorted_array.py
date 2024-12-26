class Solution:
    def kthMissing(self, arr, k):
        size = len(arr)
        i  = 1
        out = []
        count = 0
        ans = 0
        
        for x in range(0, size):
            
            while i < arr[x]:
                
                count += 1
                out.append(i)
                i += 1
                if count == k:
                    ans = out[count-1]
                
            i += 1
        
        if len(out) < k:
            ans = arr[size-1] + (k - len(out))
        
        return ans