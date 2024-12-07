from collections import Counter

class Solution:
    def nonRepeatingChar(self,s):
        a=Counter(s)
        for i,j in a.items():

            if j==1:

                return i

                break

        return '$'