class Solution:
    def sumXOR(self, arr, n):
        sum_val = 0
        n = len(arr)
        for i in range(32):
            zc = 0  
            oc = 0

            id_sum = 0

            for j in range(n):
                if arr[j] % 2 == 0:
                    zc += 1
                else:
                    oc += 1
                arr[j] //= 2

            id_sum = oc * zc * (1 << i)

            sum_val += id_sum

        return sum_val