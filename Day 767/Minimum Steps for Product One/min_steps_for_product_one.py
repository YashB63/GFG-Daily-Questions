class Solution:
    def makeProductOne(self, arr, n):
        add = 0
        nev = 0
        zero = 0
        
        for ele in arr:
            if ele == 0:
                add += 1
                zero += 1
            elif ele > 0:
                add += ele - 1
            else:
                add += abs(ele + 1)
                nev += 1
        if nev & 1:
            add += 0 if zero != 0 else 2
        return add