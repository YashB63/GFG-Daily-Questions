def pair_sum(dict, N, arr, sum):
    for i in range(0, N):
        for j in range(i + 1, N):
            if arr[i] + arr[j] == sum:
                return True
    return False