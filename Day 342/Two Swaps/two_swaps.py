class Solution:
    def checkSorted(self,arr): 
        nbad = ibad = 0
        for i, x in enumerate(arr):
            if x != i + 1:
                ibad = i
                nbad += 1
                if nbad > 4: return False
        if nbad == 3 or nbad == 0: return True
        if nbad != 4: return False
        return arr[arr[ibad] - 1] == ibad + 1