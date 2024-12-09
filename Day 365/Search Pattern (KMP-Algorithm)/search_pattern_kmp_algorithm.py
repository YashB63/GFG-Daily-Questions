class Solution:
    def search(self, pat, txt):
        indices = []
        len_txt = len(txt)
        len_pat = len(pat)
        for i in range(len_txt - len_pat + 1):
            if txt[i:i+len_pat] == pat:
                indices.append(i)
        return indices