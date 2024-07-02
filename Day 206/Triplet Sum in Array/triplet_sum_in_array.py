class Solution:
     
    # Should return true if there exists a triplet in the
    # array arr[] which sums to x. Otherwise false
    def find3Numbers(self, arr, n, x):
        
        A.sort()
        for i in range(n-2):
            left =i+1
            right =n-1
            while left<right:
                current_sum = A[i]+A[left]+A[right]
                if current_sum==X:
                  return True
                elif current_sum < X:
                  left +=1
                else:
                  right -=1
        return False 