def remove_target(main:str, target: str)->str:
    return main - target



def remove_target1(main, target)->str:
    result = ""
    for m in main:
        for t in target:
            if m != t:
                result += m
            else:
                continue
    return result

print(remove_target1("communications", "com"))


wrong code above