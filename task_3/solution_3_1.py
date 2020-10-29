m = input()
i = ''
a = ''
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
# я обнаружила косяк: чтобы работало с длинными последовательностями надо заменить
i = i+str(num) на i = i+' '+str(num)+' '
if not str(g) in i: на if not ' '+str(g)+' ' in i:

