from math import gcd

class Solution:
	def LargestFraction(self, n, d):
        low_p,low_q = 0,1
        high_p,high_q = 1,1
        max_p,max_q = 0,1
        while True:
            mid_p = low_p + high_p
            mid_q = low_q + high_q
            if mid_q > 10000:
                break
            if mid_p*d < n*mid_q:
                max_p,max_q = mid_p,mid_q
                low_p,low_q = mid_p,mid_q
            else:
                high_p,high_q = mid_p,mid_q
                
        return max_p,max_q