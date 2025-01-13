class Solution:
    def distinct(self, M, N):
        element_count = {M[0][i]: 1 for i in range(N)}
        
        for i in range(1, N):  
            current_row_set = set(M[i])
            
            for key in list(element_count.keys()):
                if key in current_row_set:
                    element_count[key] += 1
                else:
                    del element_count[key]
        
        return sum(1 for count in element_count.values() if count == N)
