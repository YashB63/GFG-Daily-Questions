class Solution:
      
    def findTriplets(self, arr, n):
        
        for i in range(n - 1):
            X = set()
            for j in range(i + 1, n):
                y = -(arr[i] + arr[j])
                if y in X:
                    return 1
                else:
                    X.add(arr[j])
                    
        return 0