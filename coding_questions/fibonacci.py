def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)

def fibonacci2(n):
    n1 = 0
    n2 = 1
    print (n1,n2, end = " ")
    for i in range(2, n):

        n3 = n1 + n2

        n1 = n2
        n2 = n3
        print(n3, end=" ")



fibonacci2(3)