def encode(arr):
    
    encoded = ""
    i = 0
    while i < len(arr):
        count = 1
        while i + 1 < len(arr) and arr[i] == arr[i + 1]:
            i += 1
            count += 1
        encoded += arr[i] + str(count)
        i += 1
    return encoded