def even_odd_arrangement(num:int)->int:
    numbers = str(num)
    evens = []
    odds = []

    for i, n in enumerate(numbers):
        if i % 2 ==0:
            evens.append(n)
        else:
            odds.append(n)
    return int("".join(evens) + "".join(odds))

def rearrange_digits(s: str) -> str:
    even_pos = []
    odd_pos = []

    for i in range(len(s)):
        if i % 2 == 0:   # even index
            even_pos.append(s[i])
        else:            # odd index
            odd_pos.append(s[i])

    return "".join(even_pos) + "".join(odd_pos)
