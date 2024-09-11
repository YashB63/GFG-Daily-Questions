class Solution:
    def leftElement(self,arr) -> int:
        arr.sort()
        return arr[(len(arr)-1)//2]