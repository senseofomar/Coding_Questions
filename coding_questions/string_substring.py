


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

