class Solution:
    def prefixAvg(self, arr):
        list1 = [arr[0]]
        sum = arr[0]
        for i in range(len(arr)-1):
            sum = sum + arr[i+1]
            list1.append(sum//(i+2))
        return list1