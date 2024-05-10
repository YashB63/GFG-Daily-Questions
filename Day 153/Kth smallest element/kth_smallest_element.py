class Solution:
    def kthSmallest(self,arr, l, r, k):
        sorted_arr = sorted(arr)
        return sorted_arr[k - len(arr) - 1]