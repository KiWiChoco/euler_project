
def sum_digit(number):
    return sum(map(int,str(number)))

summa = 0

for a in range(1,101,1):
    for b in range(1,101,1):
        if sum_digit(a**b) > summa:
            summa = sum_digit(a**b)

print(summa)




