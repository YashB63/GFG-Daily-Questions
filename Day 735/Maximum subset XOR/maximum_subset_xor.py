class Solution:
    def maxSubsetXOR(self, arr, N):
        index = 0
        for i in range(31, -1, -1):
            max_index = index
            max_element = -float('inf')
            for j in range(index, N):
                if (arr[j] & (1 << i)) != 0 and arr[j] > max_element:
                    max_element = arr[j]
                    max_index = j
            if max_element == -float('inf'):
                continue
            arr[index], arr[max_index] = arr[max_index], arr[index]
            max_index = index
            for j in range(N):
                if j != max_index and (arr[j] & (1 << i)) != 0:
                    arr[j] ^= arr[max_index]
            index += 1
        result = 0
        for i in range(N):
            result ^= arr[i]
        return result