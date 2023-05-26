def pisz(tekst,n):
    for i in range(n):
        print(tekst)
def pisz_rek(tekst,m):
    if n>0:
        print(tekst)
        pisz_rek(telst, n-1)
def silnia_rek(n):
    if n == 0:
        return 1
    else:
        return n*silnia_rek(n-1)
print(silnia_rek(20))