class Solution:
    def printArr(self, n, arr):
        
        for i in range(n):
            print(arr[i],end=" ")
        print()

    def setToZero(self, n, arr):
        
        for i in range(n):
            arr[i]=0

    def xor1ToN(self, n, arr):
        
        for i in range(n):
            arr[i] ^= i