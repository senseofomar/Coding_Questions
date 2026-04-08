def string_to_decimal(Str:str)->int:
    vowels = "aeiou"
    binary_str = ""

    for ch in Str:
        if ch in vowels:
            binary_str += "0"
        else:
            binary_str += "1"

    decimal_num = int(binary_str, 2)
    return decimal_num

print(string_to_decimal("zoo"))




