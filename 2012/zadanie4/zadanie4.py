"""
zadanie 4, matura 2012 pp
"""


def suma_cyfr(n):
    suma = 0
    d = len(n)
    for i in range(d):
        suma += int(n[i])
    return suma


def rosnąca(n):
    rosn = True
    d = len(n)
    for i in range(0, d-1):
        if n[i] < n[i+1]:
            continue
        else:
            rosn = False
            break
    return rosn


licznik1 = 0
max = 0
maxL = 0
min = 999999999
minL = 0
lista3 = []
with open("cyfry.txt", "r") as file:
    for L in file:
        L = L.strip()
        # 4.1
        if int(L) % 2 == 0:
            licznik1 += 1
        # 4.2
        if int(suma_cyfr(L)) > max:
            max = suma_cyfr(L)
            maxL = L
        if int(suma_cyfr(L)) < min:
            min = suma_cyfr(L)
            minL = L
        # 4.3
        if rosnąca(L):
            lista3.append(L)


with open("wyniki4.txt", "w") as odp:
    odp.write("4.1\n" + str(licznik1))
    odp.write("\n\n4.2\n" + "największa: " + str(maxL) + "\n" + "najmniejsza: " + str(minL))
    odp.write("\n\n4.3\n")
    for x in range(len(lista3)):
        odp.write(lista3[x] + "\n")