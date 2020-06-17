"""
Algorytm z zadania 2.2. w Pythonie
"""
n=int(input("Wpisz dowolną liczbę naturalną:"))
jest=False
fir = 1
k = [1]
l = [1]
while fir!=n:
    fir+=1
    k.append(fir)
    l.append(fir)
if n%4==1:
    for L in k:
        for M in l:
            if n==L*L+M*M:
                jest=True
                break
if jest==True:
    print("TAK")
else:
    print("NIE")
