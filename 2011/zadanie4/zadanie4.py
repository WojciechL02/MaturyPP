"""
zadanie 4, matura 2011 pp
"""

licznikP = 0
licznikNP = 0
tablica2 = []
tablica3 = []
znak = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ASCII = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
with open("hasla.txt", "r") as file:
    for L in file:
        L = L.strip()
        # 4.1
        if len(L) % 2 == 0:
            licznikP += 1
        else:
            licznikNP += 1
        # 4.2
        if L == L[::-1]:
            tablica2.append(L)
        # 4.3
        suma = 0
        for x in range(len(L)-1):
            for i in range(len(znak)-1):
                if L[x] == znak[i]:
                    suma += ASCII[i]
            for n in range(len(ASCII)-1):
                if L[x+1] == znak[n]:
                    suma += ASCII[n]
                    if suma == 220:
                        tablica3.append(L)
                        suma = 0
                        break
                    else:
                        suma = 0


with open("wyniki4.txt", "w") as odp:
    odp.write("4.1\n" + "nieparzysta: " + str(licznikNP) + "\n" +
              "parzysta: " + str(licznikP))
    odp.write("\n\n4.2\n")
    for x in tablica2:
        odp.write(str(x) + "\n")
    odp.write("\n\n4.3\n")
    for x in tablica3:
        odp.write(str(x) + "\n")