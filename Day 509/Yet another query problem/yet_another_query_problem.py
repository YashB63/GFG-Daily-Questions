from typing import List

class Solution:
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        max_k = N
        answers = [[0] * (max_k + 1) for _ in range(N)]
        freq_map = {}
        
        for i in range(N - 1, -1, -1):
            freq_map[A[i]]=freq_map.get(A[i],0)+1
            for k in range(1, max_k + 1):
                answers[i][k] = answers[i + 1][k] if i + 1 < N else 0
                if freq_map[A[i]] == k:
                    answers[i][k] += 1
    
        result = []
        for L, R, K in Q:
            result.append(answers[L][K] - (answers[R + 1][K] if R + 1 < N else 0))
        
        return result