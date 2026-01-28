class Solution:
    def removeConsonants(self, s):
        vowels = "aeiou"
        res = ""
        
        for i in s:
            if(i.lower() in vowels):
                res = res + i
        
        return res if res else "No Vowel"