"""
algorytm 1.3
"""


k = 7
wk = 0
k_1 = 1
k_2 = 1
k_3 = 1
i = 4
while i <= k:
    if i % 2 == 0:
        wk = k_1 + k_2 + k_3
    else:
        wk = k_1
    k_3 = k_2
    k_2 = k_1
    k_1 = wk
    i += 1
print(wk)