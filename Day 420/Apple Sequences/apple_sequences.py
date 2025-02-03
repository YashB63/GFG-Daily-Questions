class Solution:
    def appleSequences(self, n, m, arr):
        j=0
        orange=0
        total=0
        for i in range(n):
            if arr[i] =='O':
                orange = orange+1
                while orange >m:
                    if arr[j] =='O':
                        orange = orange-1
                    j=j+1
            total= max(total, i-j+1)
        return total