output =''
for r in 'k'*10:
    form = ''
    lemma = ''
    id = ''
    switch = 0
    a = input()
    b = 0
    if a != '':
        for i in 'u'*len(a):
            if a[0] != '#' and a[b] != '\t' and switch == 0:
                id += a[b]
                b = b+1
            elif a[b] == '\t' and switch == 0:
                switch = 1
                b = b+1 
            elif a[b] != '\t' and switch == 1:
                form += a[b]
                b = b+1
            elif a[b] == '\t' and switch == 1:
                switch = 2
                b = b+1
            elif a[b] != '\t' and switch == 2:
                lemma += a[b]
                b = b+1
            elif a[b] == '\t' and switch == 2:
                switch = 3
            g = -1
            e = 1
            for l in 'L'*len(lemma):
                g = g+1
                if len(lemma) <= len(form):
                    if lemma[g] != form[g]:
                        e = 0
                else: 
                    e = 0
        if form != lemma and e == 0:
            output += '\t'*2+form+' '+lemma
string = ''
start = 2
if output != '':
    for f in 'F'*len(output):
        if output != '':
            if start != (len(output)-1):
                if (output[start-1] == '\t' or output[start] != '\t' or output[start+1] != '\t'):
                    string += output[start]
                    start = start+1
                else:
                    print(string)
                    string = ''
                    start = start+2
    print(string+output[(len(output)-1)])
