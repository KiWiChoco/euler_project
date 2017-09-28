
n=1

list1=[] #첫 수의 약수 그룹
list2=[] #약수의 약수 그룹
list3=[] #친화수 그룹

while n<1001:

    n=n+1
    
    for i in range(1,n):
        if n%i==0:
            list1.append(i)

    sum_list1=sum(list1)

    for j in range(1,sum_list1):
        if sum_list1%j==0:
            list2.append(j)

    sum_list2=sum(list2)


#print(sum_list1,sum_list2)

#if n==sum_list2:
#    print('amicable number')

    

    if n==sum_list2:
        list3.append(n)



print(list3)
        
