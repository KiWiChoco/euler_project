import math


# all_count = 0
count = 0

for i in range(23,101,1):
    #count = 0
    for j in range(1,i,1):
        if math.factorial(i)/(math.factorial(j)*math.factorial(i-j)) > 1000000:
            count +=1
    #all_count += count*2

print(count)