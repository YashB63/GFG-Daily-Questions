class Solution:
    def knightInGeekland(self, arr, start):
        m, n = len(arr), len(arr[0])
        q = [(start[0], start[1])]
        coins = []
        visited = {(start[0], start[1])}
        
        ds = [(r, c) for r in (-2, 2) for c in (-1, 1)] + [(r, c) for r in (-1, 1) for c in (-2, 2)]
        while q:
            s = 0
            nq = []
            for r0, c0 in q:
                s += arr[r0][c0]
                for dr, dc in ds:
                    r, c = r0+dr, c0+dc
                    if (r, c) not in visited and 0 <= r < m and 0 <= c < n:
                        nq.append((r, c))
                        visited.add((r, c))
            coins.append(s)
            q = nq
        
        cnt = 0
        ans = 0
        for i in range(len(coins)-1, -1, -1):
            if coins[i]+i < len(coins):
                coins[i] += coins[coins[i]+i]
            if coins[i] >= cnt:
                cnt = coins[i]
                ans = i
        return ans