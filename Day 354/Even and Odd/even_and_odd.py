class Solution:
    def reArrange(self, arr, N):
        even_index = 0
        odd_index = 1
        
        while even_index < N and odd_index < N:
            if arr[even_index] % 2 == 0:
                even_index += 2
            elif arr[odd_index] % 2 == 1:
                odd_index += 2
            else:
                arr[even_index],arr[odd_index] = arr[odd_index], arr[even_index]
                even_index += 2
                odd_index += 2
        return arr