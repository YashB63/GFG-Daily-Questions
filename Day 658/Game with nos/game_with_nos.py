def game_with_number(arr, n):
    for d in range(n - 1):  
        arr[d] = arr[d] ^ arr[d + 1]  
    return arr  