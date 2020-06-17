"""
algorytm z zadania 1.3.,  matura 2017 pp cz. 1
"""

d = 21
k = 2
n = 2
s = ["e", "i", "i", "n", "d", "a", "e", "z", "o", "t", "i", "n", "w", "e", "z", "s", "s", "y", "k", "t", "p", "o"]
i = 0
while i < d-k-n:
    i = i+n
print(i)
z = " "
while i >= 0:
    z = s[i]
    s[i] = s[i+k]
    s[i+k] = z
    i = i-n
print(s)