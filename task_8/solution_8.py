N = int(input())
quant = 0
sum = 0
g = 0
for d in 'D'*N:
    if g != 1:
        num = int(input())
        if num != 0:
            sum = sum+num
            quant += 1
        else: 
            g = 1
if quant == N:
    print('no!')
else:
    print(sum/quant)
