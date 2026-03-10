def checksum_sum(nums: list[int]) -> int:
    total_sum = 0  # this will store final answer

    for num in nums:
        # Step 1: convert number into list of digits

        digits = list(map(int, str(num)))
        # Example: 1223 → ['1','2','2','3'] → [1,2,2,3]
        if len(digits) <= 2:
            continue  # checksum = 0

        # Step 2: find min and max digit
        min_digit = min(digits)
        max_digit = max(digits)

        # Step 3: remove one occurrence of min and max
        digits.remove(min_digit)
        digits.remove(max_digit)

        # Step 4: checksum = sum of remaining digits
        total_sum += sum(digits)

    return total_sum
