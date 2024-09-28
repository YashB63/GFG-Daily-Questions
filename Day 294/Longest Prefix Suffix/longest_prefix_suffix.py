class Solution:
	def lps(self, str):
        pi = [0] * len(s)
        idx = 1
        k = 0
        while idx < len(s):
            if s[idx] == s[k]:
                pi[idx] = k + 1
                k += 1
                idx += 1 
            else:
                if k == 0:
                    pi[idx] = 0
                    idx += 1
                else:
                    k = pi[k - 1]
        return pi[-1]