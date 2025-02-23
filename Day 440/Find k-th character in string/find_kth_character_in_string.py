class Solution:
	def kthCharacter(self, m, n, k):
        m = bin(m)[2:]
        flag = True
        k-=1
        for _ in range(n):
            if k % 2 != 0:
                flag = not flag
            k //= 2
        return int(m[k]) if flag else int(not int(m[k]))