class Solution:
    def maxSumBitonicSubArr(self, arr):
        n = len(arr)

        max_sum = arr[0]
        current_sum = arr[0]
        flag = 0  

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                if flag == 2:
                    current_sum = arr[i - 1] + arr[i]
                else:
                    current_sum += arr[i]
                flag = 1
            elif arr[i] < arr[i - 1]:
                current_sum += arr[i]
                flag = 2
            else:
                if flag == 2:
                    max_sum = max(max_sum, current_sum)
                    current_sum = arr[i]
                else:
                    current_sum += arr[i]
                    
            max_sum = max(max_sum, current_sum)

        return max_sum