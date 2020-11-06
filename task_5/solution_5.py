front_vow = 'eiöü'
back_vow = 'aıou'
yes = 0
no = 0
for r in 'k'*10:
    k = 0
    G = 0
    vow_in_lemma = ''
    vow_in_form = ''
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
             if len(form) >= len(lemma):
                 if lemma[g] != form[g]:
                     e = 0 
             else:
                 e = 0
        g = 0
        if form != lemma and e == 1:
            for s in 'S'*len(lemma):
                if lemma[g] in front_vow+back_vow:
                    vow_in_lemma += lemma[g]
                    g += 1
                else:
                    g += 1
            for s in 'S'*len(form):
                if form[G] in front_vow+back_vow:
                    vow_in_form += form[G]
                    G += 1
                else:
                    G += 1
            for s in 'S'*len(vow_in_form):
                if bool(vow_in_form[k] in back_vow) == bool(vow_in_form[len(vow_in_lemma)-1] in back_vow):
                    yes += 1
                    k += 1
                else:
                    no += 1
                    k += 1
print('vowel_harmony ',yes)
print('no_vowel_harmony ',no)
