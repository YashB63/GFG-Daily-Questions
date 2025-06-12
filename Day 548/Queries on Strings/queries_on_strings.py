class Solution:
    def SolveQueris(self, str, Query):
        results = []

        for query in Query:
            l = query[0] - 1  
            r = query[1] - 1  
            unique_chars = set()

            for i in range(l, r + 1):
                unique_chars.add(str[i])

            results.append(len(unique_chars))

        return results