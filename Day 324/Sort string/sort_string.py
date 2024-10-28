import itertools

class Solution:
    def SortedString(self, s: str) -> str:
        vowels = "aeiou"
        
        vow = [sym for sym in s if sym in vowels ]
        
        con = [sym for sym in s if sym not in vowels]
        
        vow.sort()
        
        con.sort()
        
        if s[0] in vowels:
            return "".join(sym[0] + sym[1] for sym in itertools.zip_longest(vow, con, fillvalue=""))
            
        else:
             return "".join(sym[1] + sym[0] for sym in itertools.zip_longest(vow, con, fillvalue=""))