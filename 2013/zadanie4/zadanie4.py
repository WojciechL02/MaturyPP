"""
zadanie 4, matura 2013 pp
"""


def tyle_samo(n):
    l1 = 0
    l0 = 0
    d = len(n)
    for i in range(d):
        if n[i] == "1":
            l1 += 1
        else:
            l0 += 1
    if l0 == l1:
        return True
    else:
        return False


def czy_same_0(n):
    licz = 0
    d = len(n)
    for i in range(d):
        if n[i] == "0":
            licz += 0
        else:
            licz += 1
    if licz == 0:
        return True
    else:
        return False


def czy_same_1(n):
    d = len(n)
    licz = 0
    for i in n:
        if i == "0":
            break
        else:
            licz += 1
    if licz == d:
        return True


licznik1 = 0
licznik2 = 0
licznikS0 = 0
licznikS1 = 0
lista4 = []
for i in range(17):
    lista4.append(0)

with open("napisy.txt", "r") as file:
    for N in file:
        N = N.strip()
        # 4.1
        d = len(N)
        if d % 2 == 0:
            licznik1 += 1
        # 4.2
        if tyle_samo(N):
            licznik2 += 1
        # 4.3
        if czy_same_0(N):
            licznikS0 += 1
        if czy_same_1(N):
            licznikS1 += 1
        # 4.4
        d = len(N)
        for k in range(2, d+1):
            if k == d:
                lista4[k] += 1


with open("wyniki4.txt", "w") as odp:
    odp.write("4.1\n" + str(licznik1))
    odp.write("\n\n4.2\n" + str(licznik2))
    odp.write("\n\n4.3\n" + "same zera: " + str(licznikS0) + "\n"
              "same jedynki: " + str(licznikS1))
    odp.write("\n\n4.4\n")
    for i in range(2,17):
        odp.write(str(i) + ": " + str(lista4[i]) + "\n")