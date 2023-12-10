def isPalindrome(num):
    return str(num) == str(num)[::-1]
    
def PalinArray(arr ,n):
    for num in arr:
        if not isPalindrome(num):
            return 0
    return 1