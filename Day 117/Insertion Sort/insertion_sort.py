class Solution:
    def insert(self, alist, index, n):
        
        for i in range(n - 1, index - 1, -1):
            alist[i + 1] = alist[i]
        alist[index] = n
    
    def insertionSort(self, alist, n):
        
        for i in range(1, n):
            key = alist[i]
            j = i - 1
            while j >= 0 and alist[j] > key:
                alist[j + 1] = alist[j]
                j -= 1
            alist[j + 1] = key