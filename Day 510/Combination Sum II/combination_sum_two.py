class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def backtrack(curr_sum, start, path):
            if curr_sum == target:
                res.append(path[:])
                return 
            if curr_sum > target:
                return 
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(curr_sum + candidates[i], i+1, path)
                path.pop()

            
        backtrack(0,0,[])
        return res