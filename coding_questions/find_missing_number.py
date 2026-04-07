def find_missing_sum(arr, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(arr)

    missing = expected_sum - actual_sum
    return missing


arr = [1,2,4,5]
N = 5

print(find_missing_sum(arr, N))

