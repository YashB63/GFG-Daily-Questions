class Solution:
	def countSumSubsets(self, arr, N):
        count = 0
        
        for i in range(1, 1<<N):
            temp = []
            for j in range(N):
                if (i&(1<<j)) > 0:
                    temp.append(arr[j])
                    
            if (sum(temp)%2) == 0:
                count +=1
                
        return count