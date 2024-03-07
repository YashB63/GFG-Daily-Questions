class Solution:
    def smallestNumber(self, num):

        n = len(num)
        arr = [0] * n
        midx = n - 1
        idx = 0
        
        for i in range(n - 1, -1, -1):
            if num[idx] > num[i] and num[i] != '0':
                idx = i
            if num[midx] > num[i]:
                midx = i
            arr[i] = midx
        
        num_list = list(num)
        
        if idx != 0:
            num_list[idx], num_list[0] = num_list[0], num_list[idx]
            return ''.join(num_list)
        
        for i in range(1, n):
            if num_list[i] > num_list[arr[i]]:
                num_list[i], num_list[arr[i]] = num_list[arr[i]], num_list[i]
                break
        
        return ''.join(num_list)