def fun(n):
    if n == 0:
        return 1
    else:
        return fun(n-1) + 2*n

i = int(input("Wprowadź liczbę: "))
for n in range(i):
    print(fun(n))
