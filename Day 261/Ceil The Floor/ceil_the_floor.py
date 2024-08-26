class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
        start, end = 0, len(arr)-1
        f,c = -1,-1
        while start <= end:
            mid = (end+start)//2
            if arr[mid] == x:
                f = arr[mid]
                break
            elif arr[mid] < x:
                f = arr[mid]
                start = mid + 1
            elif arr[mid] > x:
                end = mid-1
        start, end = 0, len(arr)-1
        while start <= end:
            mid = (end+start)//2
            if arr[mid] == x:
                c = arr[mid]
                break
            elif arr[mid] < x:
                start = mid + 1
            elif arr[mid] > x:
                c = arr[mid]
                end = mid-1
        return f,c