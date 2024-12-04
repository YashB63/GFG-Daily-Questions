class Solution:
    def endPoints(self, matrix, m, n):
        i,j=0,0
        direction = 'right'
        
        directions={ 'right' : (0,1),
                     'left' : (0,-1),
                     'up' : (-1,0),
                     'down': (1,0)
                    }
        direction_change = { 'right' : 'down',
                             'left' : 'up',
                             'up' : 'right',
                             'down': 'left'
                            }
        while 0<=i<m and 0<=j<n:
            if matrix[i][j]==1:
                matrix[i][j]=0
                direction = direction_change[direction]
            di,dj = directions[direction]
            new_i,new_j = i+di,j+dj
            if not (0<=new_i<m and 0<=new_j<n):
                break
            i,j = new_i,new_j
                
        return (i,j)