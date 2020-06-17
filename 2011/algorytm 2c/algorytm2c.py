"""
algorytm z zadania 2 c, matura 2011 pp
"""

lista = []
i = 2
n = 42
while i <= n:
    while n % i == 0:
        lista.append(i)
        n = n//i
    i += 1
print(lista)