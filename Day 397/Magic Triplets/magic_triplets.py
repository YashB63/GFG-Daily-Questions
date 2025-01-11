class Solution:
	def countTriplets(self, nums):
        ln = len(nums)
        res = 0
        for m in range(1, ln-1):
            m_num = nums[m]
            l_count = sum(nums[i] < m_num for i in range(0, m))
            r_count = sum(nums[i] > m_num for i in range(m+1, ln)) 
            res += l_count*r_count
            
        return res
