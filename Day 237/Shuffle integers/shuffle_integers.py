class Solution:
    def shuffleArray(self, arr, n):
        arr1 = arr[:n//2]
        arr2 = arr[n//2:]
        arr.clear()
        for i in range(n//2):
            arr.append(arr1[i])
            arr.append(arr2[i])
        return arr