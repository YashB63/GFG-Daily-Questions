class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n : int ) -> bool:
        return bin(n).count('1')==1 