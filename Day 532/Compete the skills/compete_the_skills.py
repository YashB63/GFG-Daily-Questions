class Solution:
    def scores(self, arr1, arr2):
        v = []
        ca = 0
        cb = 0

        for i in range(3):
    
            if arr1[i] > arr2[i]:
                ca += 1

            elif arr2[i] > arr1[i]:
                cb += 1

        v.append(ca)
        v.append(cb)
        return v