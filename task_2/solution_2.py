m = input()
i = ''
a = ''
for M in range(0,len(m)):
    for J in range(M+1,len(m)):
        if m[M] == m[J]:
            i = i+str(M)
for w in range(0,len(m)):
    if not str(w) in i:
        a = a + m[w]
s=a[0]
l = 0
for M in range(0,len(m)):
    if a[0] == m[M]:
        l = l+1
    k = l
for A in range(1,len(a)):
    l = 0
    for M in range(0,len(m)):        
        if a[A] == m[M]:
            l = l+1        
    if k == l:
        s = 'there.s more than one'
    elif l > k:
        s = a[A]
        k = l
print(s)
