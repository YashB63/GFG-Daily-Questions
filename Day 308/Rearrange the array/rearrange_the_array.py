class Solution:
    def rearrangeArray(self, arr):
        arr.sort()
        res = arr[:]
        n = len(arr)
        k = 0
        i = 0
        j = n - 1
        while k < n:
            arr[k] = res[i]
            if k+1 < n:
                arr[k+1] = res[j]
            k += 2
            i += 1
            j -= 1
        return arr