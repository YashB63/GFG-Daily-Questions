class Solution:
    
	def threeWayPartition(self, array, a, b):
	    
	    low = 0
        mid = 0
        high = len(array) - 1
        
        while mid <= high:
            if array[mid] < a:
                array[mid], array[low] = array[low], array[mid]
                low += 1
                mid += 1
            elif a <= array[mid] <= b:
                mid += 1
            else:
                array[mid], array[high] = array[high], array[mid]
                high -= 1
        
        return 1