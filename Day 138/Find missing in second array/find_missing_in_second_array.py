class Solution:
    def findMissing(self,a,b,n,m):

        b_set = set(b) 
        missing_elements = [x for x in a if x not in b_set]
        return missing_elements