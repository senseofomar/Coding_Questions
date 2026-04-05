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


