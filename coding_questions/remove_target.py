# best for interviews
def remove_target(main, target):

    n = len(main)
    m = len(target)

    result = ""
    i = 0

    while i < n:

        if main[i:i+m] == target:
            i += m
        else:
            result += main[i]
            i += 1

    return result


print(remove_target("communications", "com"))