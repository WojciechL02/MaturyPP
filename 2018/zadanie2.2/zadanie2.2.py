"""
algorytm z zadania 2.2
matura 2018 pp
"""
A = [1, 2, 6, 3, 4, 5, 6]
n = 7
licznik = 0
for i in range(n-1):
    m = i
    for j in range(i, n):
        if A[m] < A[j]:
            m = j
    if i != m:
        A[i], A[m] = A[m], A[i]
        licznik += 1
        print(licznik)
        print(A)