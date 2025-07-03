def firstDigit(n):
    while n > 9:
        n = n // 10
    return n