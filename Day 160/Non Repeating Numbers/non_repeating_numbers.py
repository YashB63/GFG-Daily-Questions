class Solution:
	def singleNumber(self, nums):
		
        xor_result = 0
        for num in nums:
            xor_result ^= num
        rightmost_set_bit = xor_result & -xor_result
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
        return [min(num1, num2), max(num1, num2)]