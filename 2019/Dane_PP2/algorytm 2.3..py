"""
zadanie 2.3. matura 2019 pp
"""

n = int(input("Wpisz:"))
for i in range(1, n):
    for k in range(1, n):
        if i*i + k*k == n:
            print(i, k)
            break

