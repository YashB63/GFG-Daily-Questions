class Solution:
    def search(self, pat, txt):
        
        res = []
        i = 0
        while i != -1:
            i = txt.find(pat, i)
            if i == -1:
                break
            i += 1
            res.append(i)
        return res