fact=1
for factor in range(100,1,-1):
    fact = fact * factor

list1=list(str(fact))


n = len(list1)
sum=0

for i in range(n):
    sum = sum + eval(list1[i])

print(sum)
