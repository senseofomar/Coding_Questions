

def rvn(n):
    reversen = 0
    while n>0:
        rrem = n%10
        reversen = reversen*10 + rrem

        n = n//10

    return reversen

print(rvn(12423))
