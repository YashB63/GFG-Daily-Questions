class Solution:
    def findTwoElement(self, arr):
        n = len(arr)

        S = n * (n + 1) // 2                   
        P = n * (n + 1) * (2*n + 1) // 6       

        S_arr = sum(arr)
        P_arr = sum(x*x for x in arr)

        diff = S_arr - S                           
        diff2 = (P_arr - P) // diff                
        R = (diff + diff2) // 2
        M = diff2 - R

        return [R, M]