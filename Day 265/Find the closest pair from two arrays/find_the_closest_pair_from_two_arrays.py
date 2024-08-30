class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        l=0
        r=m-1
        closest_pair = (arr[0], brr[0])
        closest_diff = sys.maxsize
        while l < n and r >= 0:
            current_sum = arr[l] + brr[r]
            current_diff = abs(current_sum - x)

            if current_diff < closest_diff:
                closest_diff = current_diff
                closest_pair = (arr[l], brr[r])

            if current_sum > x:
                r -= 1
            else:
                l += 1

        return list(closest_pair)