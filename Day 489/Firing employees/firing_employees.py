from collections import defaultdict
from collections import deque

class Solution:
    def firingEmployees(self, arr, n):
        adj = defaultdict(list)
        root = None
        for i in range(n):
            if arr[i] == 0:
                root = i + 1
            else:
                adj[arr[i]].append(i + 1)
        ans = 0
        is_prime = self.generatePrimes(2 * n)
        que = deque([(root, 0)])
    
        while que:
            node, node_height = que.popleft()
            if node_height > 0 and is_prime[node + node_height]:
                ans += 1
            for nbr in adj[node]:
                que.append((nbr, node_height + 1))
        return ans
        
    def generatePrimes(self, n):
        p = 2
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        while p * p <= n:
            if is_prime[p] == True:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return is_prime