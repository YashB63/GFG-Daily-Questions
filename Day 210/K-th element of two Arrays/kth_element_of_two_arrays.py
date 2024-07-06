class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        arr = sorted(arr1+arr2)
        return arr[k-1]