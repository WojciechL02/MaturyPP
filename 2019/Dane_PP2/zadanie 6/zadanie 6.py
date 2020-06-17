"""
zadanie 6
matura 2019 pp
"""
k = 0
m = 0
list = 0
np = []
with open("dane.txt","r") as plik:
    for P in plik:
        P = P.strip()
        #6.1
        n = int(P[-2])
        if n%2 == 0:
            k += 1
        else:
            m += 1
        #6.2
        if (P[2] == "1" or P[2] == "3") & (P[3] == "1"):
            list += 1
        #6.3
        p = int(P[0]) + 3 * int(P[1]) + 7 * int(P[2]) + 9 * int(P[3]) + 1 * int(P[4]) + 3 * int(P[5]) + 7 * int(P[6]) + 9 * int(P[7]) + 1 * int(P[8]) + 3 * int(P[9]) + int(P[10])
        if int(p)%10 != 0:
            np.append(P)

with open("wyniki6.txt","w") as plik:
    plik.write("zad 6.1"+"\n"+
               "kobiety: "+str(k)+"\n"+
               "mężczyźni: "+str(m)+"\n"+
               "zad 6.2\n"+
               str(list)+"\n"+
               "zad 6.3\n"+str(np))


