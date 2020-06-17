"""
zadanie 4, matura 2017 pp
"""


def rosnaca(a, b, c):
    if a < b and b < c:
        return True
    else:
        return False


def NWD(a, b):
    while b != 0:
        a, b = b, a%b
    return a


def NWD3(a, b, c):
    return NWD(NWD(a, b), c)


def suma_cyfr(a):
    suma3 = 0
    while a > 0:
        suma3 += a%10
        a = a//10
    return suma3


licznik1 = 0
suma2 = 0
licznik3 = 0
najw3 = 0
licznik_najw = 0
with open("Liczby.txt", "r") as fiLe:
    for Line in fiLe:
        Line = Line.strip()
        L = Line.split(" ")
        L[0] = int(L[0])
        L[1] = int(L[1])
        L[2] = int(L[2])
        # 4.1
        if rosnaca(L[0], L[1], L[2]):
            licznik1 += 1
        # 4.2
        suma2 += NWD3(L[0], L[1], L[2])
        # 4.3
        suma3 = suma_cyfr(L[0]) + suma_cyfr(L[1]) + suma_cyfr(L[2])
        if suma3 == 35:
            licznik3 += 1
        if suma3 > najw3:
            najw3 = suma3
            licznik_najw = 1
        elif suma3 == najw3:
            licznik_najw += 1


with open("wyniki4.txt", "w") as odp:
    odp.write("4.1\n"
              + str(licznik1))
    odp.write("\n\n4.2\n"
              + str(suma2))
    odp.write("\n\n4.3\n"
              + str(licznik3)
              + "\n" + str(najw3)
              + "\n" + str(licznik_najw))
