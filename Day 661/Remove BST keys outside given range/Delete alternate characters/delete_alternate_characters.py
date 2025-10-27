class Solution:
    def delAlternate(self, S: str) -> str:
        final_S = ""
        for i in range(len(S)):
            if i % 2 == 0:
                final_S += S[i]
        return final_S