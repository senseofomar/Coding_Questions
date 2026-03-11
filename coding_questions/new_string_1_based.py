def new_string(s1: str, s2: str) -> str:
    result = ""
    for i, ch in enumerate(s2):
        if ch == '1':
            result += s1[i]
    return result

def new_string2(s1: str, s2: str) -> str:
    result = ""
    for ch1, ch2 in zip(s1, s2):
        if ch2 == '1':
            result += ch1
    return result


def new_string3(s1, s2):
    return "".join(c1 for c1, c2 in zip(s1, s2) if c2 == '1')

