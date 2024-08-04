class Solution:

	def rowWithMax1s(self,arr):
        counts = [0] * len(arr)  
        max_count = -1
        max_row_index = -1
        
        for i, row in enumerate(arr):
            count = row.count(1)
            counts[i] = count
            
            if count > max_count and count != 0:
                max_count = count
                max_row_index = i
        
        return max_row_index