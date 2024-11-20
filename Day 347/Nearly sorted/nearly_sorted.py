class Solution:
    def rearrangeArray(self, arr):
        for i in range(len(arr)):
            if (i + 1)%2==0:
                if arr[i] < arr[i - 1]:
                    arr[i],arr[i - 1]=arr[i - 1],arr[i]
            else:
                if arr[i] > arr[i - 1]:
                    arr[i],arr[i - 1]=arr[i - 1],arr[i]
        return arr