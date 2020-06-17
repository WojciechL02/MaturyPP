"""
zadanie 6, matura 2016 pp
"""


def pierwsza(L):
    pierw = True
    i = 2
    while i <= int(L/2+1):
        if L % i == 0:
            pierw = False
            break
        else:
            i += 1
    return pierw


min2 = 30000
max2 = 0
licznik1 = 0
p1 = 0
p2 = 0
licznik3 = 0
pary = ""
with open("dane4.txt","r") as file:
    for L in file:
        L = int(L.strip())
        if pierwsza(L):
            licznik1 += 1
            if L < min2:
                min2 = L
            if L > max2:
                max2 = L
            p1 = p2
            p2 = L
            if abs(p1 - p2) == 2:
                licznik3 += 1
                pary = pary+str(p1) + " " + str(p2) + "\n"



with open("wyniki_6.txt", "w") as odp:
    odp.write("6.1\n" + str(licznik1))
    odp.write("\n\n6.2\n" + str(min2) + "\n" + str(max2))
    odp.write("\n\n6.3\n" + "ilość:" + str(licznik3)+ "\n" + pary)
