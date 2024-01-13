class Solution:
    def subArraySum(self,arr, n, s): 
       
        i = 1
        j = 0
       
        curr = arr[0]
       
        while curr != s:
            if curr < s:
                if i == n:
                   return [-1]
                   
                curr += arr[i]
                i += 1
            
            else:
                curr -= arr[j]
                j += 1
        
        return [j + 1, i] if j != i else [-1]