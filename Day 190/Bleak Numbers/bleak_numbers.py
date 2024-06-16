from math import log2

class Solution:
	def is_bleak(self, n):
		
		num_bits = int(log2(n)) + 1

        for candidate in range(n - num_bits, n + 1):
            sum_of_bits = candidate + bin(candidate).count('1')

            if sum_of_bits == n:
                return 0

        return 1