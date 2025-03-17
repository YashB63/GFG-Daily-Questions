class Solution:
    def convertMinToMaxHeap(self, n, arr):
        def heapify(i):
            largest=i
            l=2*i+1
            r=2*i+2
            if l<n and arr[l]>arr[largest]:
                largest=l 
            if r<n and arr[r]>arr[largest]:
                largest=r 
            if largest!=i:
                arr[i],arr[largest]=arr[largest],arr[i]
                heapify(largest)
        for i in range(n//2-1,-1,-1):
            heapify(i)