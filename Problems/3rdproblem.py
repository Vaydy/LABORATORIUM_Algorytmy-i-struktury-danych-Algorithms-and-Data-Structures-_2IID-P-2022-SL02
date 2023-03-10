n = int(input())
temperatury = list(map(int, input().split()))
x = int(input())

licznik = 0
dni = []
for i in range(n):
    if temperatury[i] == x:
        licznik += 1
        dni.append(i+1)

print(licznik)
print(*dni)
