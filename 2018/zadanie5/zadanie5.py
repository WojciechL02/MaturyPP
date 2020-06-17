"""
zadanie 5 matura 2018 pp
"""

def suma_cyfrL(n):
    suma = 0
    while n>0:
        suma += n%10
        n = n//10
    return suma

def suma_cyfrT(n):
    suma = 0
    for C in n:
        suma += int(C)
    return suma

najw = 0
suma_wszystkich = 0
pal = []
more30 = []
with open("liczby.txt", "r") as file:
    for L in file:
        # 5.2
        L = L.strip()
        if L == L[::-1]:
            pal.append(int(L))
        # 5.1
        L = int(L)
        if L%2 == 0:
            if L > najw:
                najw = L
        # 5.3
        s = suma_cyfrL(L)
        if s > 30:
            more30.append(L)
        suma_wszystkich += s

with open("wyniki5.txt", "w") as odp:
    odp.write("5.1\n"
              + str(najw)
              + "\n\n5.2\n"
              + str(pal)
              + "\n\n5.3\n"
              + str(more30)
              + "\nsuma = "
              + str(suma_wszystkich))
