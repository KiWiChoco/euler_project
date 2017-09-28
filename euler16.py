list1=list(str(2**1000))

print(list1)

n = len(list1)
sum=0

for i in range(n):
    sum = sum + eval(list1[i])

print(sum)
