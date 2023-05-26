def szybkie_pot(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = szybkie_pot(x, int(n/2))
        return y * y
    else:
        y = szybkie_pot(x, (n-1)/2)
        return x * y * y
print(szybkie_pot(2,30))
print(szybkie_pot(11,123))