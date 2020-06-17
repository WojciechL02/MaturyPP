"""
zadanie 5, matura 2015 pp
"""

lista1 = []
for i in range(13):
    lista1.append(0)

wydruk = ""
lista2 = []
lista2o = []
listaX = []
listaS = []

with open("nowe.txt", "r") as plik2:
    for X in plik2:
        listaX.append(X.strip())
        lista2.append(0)
        lista2o.append(0)

with open("slowa.txt", "r") as plik1:
    for S in plik1:
        S = S.strip()
        listaS.append(S)
        d = len(S)
        lista1[d] += 1

i = 0
for X in listaX:
    for S in listaS:
        if X == S:
            lista2[i] += 1
        if X[::-1] == S:
            lista2o[i] += 1
    wydruk = wydruk + X + " " + str(lista2[i]) + " " + str(lista2o[i]) + "\n"
    i += 1


with open("wyniki5.txt", "w") as odp:
    odp.write("5.1\n")
    for i in range(1,13):
        odp.write(str(i) + ": " + str(lista1[i]) + "\n")
    odp.write("\n5.2\n" + wydruk)