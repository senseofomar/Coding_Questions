def find_missing_sum(arr, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(arr)

    missing = expected_sum - actual_sum
    return missing


arr = [1,2,4,5]
N = 5

print(find_missing_sum(arr, N))

def find_missing_xor(arr, N):

    xor_all = 0
    xor_arr = 0

    for i in range(1, N+1):
        xor_all ^= i

    for num in arr:
        xor_arr ^= num

    missing = xor_all ^ xor_arr

    return missing


arr = [1,2,4,5]
N = 5

print(find_missing_xor(arr, N))