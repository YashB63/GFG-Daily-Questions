class Solution:
	def sentencePalindrome(self, s):
		
		new = ''
		for a in s:
		    if a.isalpha() or a.isdigit():
		        new += a.lower()
	    return new == new[::-1]