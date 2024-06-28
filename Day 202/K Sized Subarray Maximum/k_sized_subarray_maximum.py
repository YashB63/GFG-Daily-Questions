from collections import deque

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        result = []
        dq = deque()
    
    # Process first k elements of array
        for i in range(k):
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
    
    # Process rest of the elements
        for i in range(k, n):
            result.append(arr[dq[0]])
        
        # Remove elements outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()
        
        # Remove all elements smaller than the currently being added element
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
        
            dq.append(i)
    
    # Add the maximum element of last window
        result.append(arr[dq[0]])
    
        return result