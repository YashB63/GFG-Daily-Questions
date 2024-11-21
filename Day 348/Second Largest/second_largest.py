class Solution:
    def getSecondLargest(self, arr):
        unique_elements = list(set(arr))
        if len(unique_elements) < 2:
            return -1
        unique_elements.sort()
        
        return unique_elements[-2]