class Solution:
    def find_height(self,tree,n,k):
        def get_wood(h):
            nonlocal tree
            w = 0
            for t in tree:
                if t > h:
                    w += t-h
            return w
        
        low, high = 0, max(tree)
        best_ = -1
        while low <= high:
            mid = (low + high) // 2
            wood = get_wood(mid)
            if wood == k:
                return mid
            if wood > k:
                low = mid + 1
            else:
                high = mid - 1
        return best_