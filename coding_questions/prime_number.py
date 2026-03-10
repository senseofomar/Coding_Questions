def prime(num:int)-> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) +1):
         if num%i == 0:
             return False

    return True

num = int(input("enter your number: "))

if prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# p1
def prinecheck(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i ==0:

            return False
    return True

print(prinecheck(47))