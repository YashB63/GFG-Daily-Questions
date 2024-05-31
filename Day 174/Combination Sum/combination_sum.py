class Solution:
    
    def combinationalSum(self,A, B):
       
        def find_combinations(A, target, start, path, result):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(A)):
                if A[i] > target:
                    break
                find_combinations(A, target - A[i], i, path + [A[i]], result)

        A=sorted(set(A))
        result = []
        find_combinations(A, B, 0, [], result)
        return result