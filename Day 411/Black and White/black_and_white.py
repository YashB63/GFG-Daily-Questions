def numOfWays(M, N):
    x_off = [-2,-2,-1, 1, 2, 2, 1, -1]
    y_off = [-1, 1, 2, 2, 1,-1, -2, -2]
    MOD = 1000000007
    res = 0
    for i in range(m):
        for j in range(n):
            for k in range(8):
                x = i + x_off[k]
                y = j + y_off[k]
                if x>=0 and x<m and y>=0 and y<n :
                    res+=1 
    total = ((m*n)*(m*n-1))%MOD 
    return (total +MOD - res)%MOD