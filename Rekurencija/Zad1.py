def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a
def nwd_r(a,b):
    if b!=0:
        return nwd_r(b,a%b)
    else:
        return a
def mwd_i2(a,b):
    while b!=a:
        return a
def nwd_r2(a,b):
    id a==b:
    return a
    elif a>b:
        return nwd_r2(a-b,b)
    else:
        return nwd_r2(a,b-a)
print(nwd_r(24,36))
print(nwd_i(24,36))