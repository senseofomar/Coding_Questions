# best interview approach, fully logic based no slicing
def substring_finder(s, subs):

    n = len(s)
    m = len(subs)

    for i in range(n - m + 1):

        match = True  #Assume it matches unless proven otherwise

        for j in range(m):

            if s[i + j] != subs[j]:
                match = False
                break

        if match:
            return True

    return False


print(substring_finder("hello world", "hello"))


# second best approach using slicing
def contains_substring(string, substring):

    n = len(string)
    m = len(substring)

    for i in range(n - m + 1):

        if string[i:i+m] == substring:
            return True

    return False


string = "Hello World"

print(contains_substring(string, "Hello"))
print(contains_substring(string, "World"))

# pythonic way
def contains_substring1(string, substring):
    return substring in string


string = "Hello World"

print(contains_substring1(string, "Hello"))
print(contains_substring1(string, " World"))

