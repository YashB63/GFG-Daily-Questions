class Solution:
    def Anagrams(self, words, n):
        
        d={}
        for i in words:
            if "".join(sorted(i)) not in d.keys():
               d["".join(sorted(i))]=[i]
            else:
                d["".join(sorted(i))].append(i)
        
        return d.values()
