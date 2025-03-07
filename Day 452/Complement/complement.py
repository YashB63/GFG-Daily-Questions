class Solution:

	def findRange(self,a, size):
        total = 0
        curr_count = 0
        l = 0
        ans = [-1]
        for r, c in enumerate(a):
                if c == '1':
                    curr_count -= 1
                if c == '0':
                    curr_count += 1
                if curr_count > total:
                    total = curr_count
                    ans = [l+1, r+1]
                if curr_count < 0:
                    curr_count = 0
                    l = r+1
        return ans