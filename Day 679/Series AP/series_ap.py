class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        difference=a2-a1
        nthTerm=a1+(n-1)*difference
        return nthTerm