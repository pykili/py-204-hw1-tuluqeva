for f in 'F'*10:
    m = input()
    i = ''
    num = 0
    g = 0
    for M in 'M'*(len(m)-1):
        k = 1
        for J in 'J'*(len(m)-num-1):
            if m[num] == m[num+k]:
                i = i+str(num)
                k += 1
            else:
                k += 1
        num += 1
    for w in 'W'*len(m):
        if not str(g) in i:
            a = a + m[g] 
        g += 1 
print(a)
num = 0
g = 0
i = ''
for M in 'M'*(len(a)-1):
    k = 1
    for J in 'J'*(len(a)-num-1):
        if a[num] == a[num+k]:
            i = i+str(num)
            k += 1
        else:
            k += 1
    num += 1
for w in 'W'*len(a):
    if not str(g) in i:
        al = al + a[g] 
    g += 1
print(al))
