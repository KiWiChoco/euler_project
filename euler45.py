thr = set()

five = set()

six = set()

for i in range(286,100000,1):
    thr.add((i*(i+1))/2)

for i in range(165,50000):
    five.add((i*(3*i-1))/2)

for i in range(143,50000):
    six.add(i*(2*i-1))




for i in thr:
    if i in five:
        if i in six:
            print(i)
            break
        else: continue
    else: continue