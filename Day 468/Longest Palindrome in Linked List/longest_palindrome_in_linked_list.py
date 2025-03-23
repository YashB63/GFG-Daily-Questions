class Solution:
    def maxPalindrome(self,head):
        arr = []
        while head:
            arr.append(head.data)
            head = head.next
        
        n = len(arr)
        max_len = 1  
    
        def is_palindrome(start, end):
            while start < end:
                if arr[start] != arr[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j):
                    max_len = max(max_len, j - i + 1)
        
        return max_len