import random
list = []
for i in range(20):
    list.append(random.randint(10, 50) )

min_wartosc = list[0]
min_pozycja = 0

for i in range(1, len(list)):
    if list[i] < min_wartosc:
        min_wartosc = list[i]
        min_pozycja = i

print("Najmniejszy element na liście to", min_wartosc, "na pozycji", min_pozycja)
print(list)