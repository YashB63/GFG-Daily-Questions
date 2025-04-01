class Solution:
    def eulerPath(self, N, graph):
        odd = 0
        for v in graph:
            if v.count(1) % 2:
                odd += 1
        return 1 if odd == 0 or odd == 2 else 0