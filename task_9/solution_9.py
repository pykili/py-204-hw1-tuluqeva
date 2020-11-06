k = 0
n = 1
for t in 'T'*100:
    k = k+(2*n-1)
    o = bool(k == n**2)
    print('for', n, 'it is', o)
    n+=1
