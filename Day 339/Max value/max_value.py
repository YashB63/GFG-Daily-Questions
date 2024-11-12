class Solution:
    def maxVal(self, arr):
        list1 = []
        for i in range(len(arr)):
            ele = arr[i] - i
            list1.append(ele)
        list1.sort()
        max = list1[-1] - list1[0]
        return max