class Solution:
    def LargestSwap(self,S):
       
        i=0
        arr = list(S)
        
        while i < len(arr):
            
            max_ = max(arr[i:])
            newarr = ''.join(arr[i:])
            ind = i + newarr.rfind(max_)

            if arr[i] != max_:
                arr[i], arr[ind] = arr[ind], arr[i]
                return ''. join(arr)

            i = i + 1

        return S
