class Solution:
    def quadraticProbing(self, arr, m):
        hash = [-1] * m  

        for num in arr:
            index = num % m

            if hash[index] == num:
                continue

            if hash[index] == -1:
                hash[index] = num
                continue

            for power in range(1, m):
                new_index = (index + power * power) % m

                if hash[new_index] == num:
                    break  

                if hash[new_index] == -1:
                    hash[new_index] = num
                    break

        return hash