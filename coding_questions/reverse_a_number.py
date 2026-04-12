def reverse_number(n:int)->str:
    num = n
    reverse = 0
    while n>0:
        remainder = n%10  #get the last digit, %10 always gives the last digit. 1234 ÷ 10 = 123 remainder 4, 17 ÷ 5 = 3 remainder 2
        reverse = (reverse*10) + remainder

        n = n//10  #removes the last digit

    return ("The given number is {} and Reverse is {}".format(num, reverse))

print(reverse_number(12234))


