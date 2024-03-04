class Solution:
	def minSteps(self, S):
		
        s = list(S)
        steps = 0
        while len(s) > 0:
            if len(s)%2 != 0:
                s.pop()
            else:
                fst = s[:len(s)//2]
                snd = s[len(s)//2:]
                if fst == snd:
                    s = fst
                else:
                    s.pop()
            steps += 1
        return steps