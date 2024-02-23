class Solution:
	def search(self, text, pat):
		
        s = ""
        for i in text:
            if len(s) < len(pat) - 1:
                s += i
            else:
                s += i
                if s == pat:
                    return 1
                s = s[1:]
        
        return 0