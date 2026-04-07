class Solution:
    def stringStack(self, pat, tar):
        i = len(pat) - 1
        j = len(tar) - 1

        while i >= 0:
            if j >= 0 and pat[i] == tar[j]:
                j -= 1 
            else:
                i -= 1 
            i -= 1 

        return j < 0