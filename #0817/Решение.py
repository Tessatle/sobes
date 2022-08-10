letters='УКЫСМ'
k=0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word=a+b+c+d+e
                    k+=1
                    if word.count('Ы')<=1 and word.count('У')==2 and word.count('С')==0:
                        print(k)
