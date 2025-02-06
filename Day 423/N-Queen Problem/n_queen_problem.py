class Solution:
    def nQueen(self, n):
        def place(rows, i):
            if i == n:
                yield rows[:]
            else:
                for c1 in range(1, n+1):
                    rows[i] = c1
                    for j in range(0, i):
                        c2 = rows[j]
                        if c1 == c2 or i-c1 == j-c2 or i+c1 == j+c2:
                            break
                    else:
                        yield from place(rows, i+1)
    
        return [e for e in place([-1]*n, 0)]