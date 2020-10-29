a = input()
start = ''
end = ''
pal = True
g = 0
for h in 'H'*len(a):
    end = a[g]+end
    if not end in a:
        pal = False
        g += 1
    else:
        g += 1
print('is_palindrom',pal)
