class Solution:
    def count_NGE(self, arr, indices):
        ans = []
        for i in indices:
            count = 0
            for j in range(i+1,len(arr)):
                if arr[i]<arr[j]:
                    count+=1
            
            ans.append(count)
        
        return ans