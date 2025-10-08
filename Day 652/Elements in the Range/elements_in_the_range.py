class Solution:
    def check_elements(self, arr, n, A, B):
        for i in range(n):
            if abs(arr[i]) >= A and abs(arr[i]) <= B:
                ind = abs(arr[i]) - A
                if ind < n and arr[ind] > 0:
                    arr[ind] = -1 * arr[ind]

        B = B - A
        
        if B > n:
            return False

        for i in range(B + 1):
            if arr[i] > 0:
                return False

        return True