def two_sum(numbers, target):
    seen = {}

    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return  [seen[complement], i]

        seen[num] = i


nums = [2,7,11,15]
print(two_sum(nums, 9))
