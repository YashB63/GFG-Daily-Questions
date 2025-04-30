class Solution:
	def ShortestDistance(self, matrix):
        m = len(matrix)
        if m == 0:
            return [[-1]]
        if m == 1:
            return [[1]]
        if matrix[0][0] == 0:
            return [[-1]]
        
        result = [[0 for _ in range(m)] for _ in range(m)]
        dirs = [(0, 1), (1, 0)]  
        
        def findShortestPath(sr, sc):
            if sr == m - 1 and sc == m - 1:
                result[sr][sc] = 1
                return True
            
            if matrix[sr][sc] == 0:
                return False
            
            result[sr][sc] = 1
            
            for rad in range(1, matrix[sr][sc] + 1):
                for d in dirs:
                    r = sr + rad * d[0]
                    c = sc + rad * d[1]
                    
                    if 0 <= r < m and 0 <= c < m:
                        if findShortestPath(r, c):
                            return True
            
            result[sr][sc] = 0
            return False
        
        if findShortestPath(0, 0):
            return result
        else:
            return [[-1]]