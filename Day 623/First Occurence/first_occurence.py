class Solution:
    def firstOccurence(self, txt, pat):
        ind_s = 0
        
        while ind_s < len(txt):

            if txt[ind_s] == pat[0]:
                ind_p = 0
                temp_s = ind_s

                while temp_s < len(txt) and txt[temp_s] == pat[ind_p]:
                    ind_p += 1
                    temp_s += 1

                    if ind_p == len(pat):
                        return ind_s
            ind_s += 1

        return -1