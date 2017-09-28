#euler 9


def euler9():
    for a in range(1,998):
        for b in range(1,999):
            for c in range(1,1000):
                if a>c or b>c: continue

                if (a+b+c==1000) and (c**2==a**2+b**2):
                    return a*b*c

                if c**2 != a**2+b**2:
                    continue
