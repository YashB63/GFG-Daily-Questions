class Solution:
    def countTriplets(self, Arr, N, L, R):
        def countTripletsUpto(X):
            count = 0
            for i in range(N - 2):
                j, k = i + 1, N - 1
                while j < k:
                    if Arr[i] + Arr[j] + Arr[k] <= X:
                        count += (k - j)  
                        j += 1
                    else:
                        k -= 1
            return count

        Arr.sort()
        return countTripletsUpto(R) - countTripletsUpto(L - 1)