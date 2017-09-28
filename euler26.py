#euler 26

list1=[] #순환마디를 가지는 수 d
list2=[] #순환마디의 길이

d=2

while d<1000:
    x=1/d
    y=str(x)
    print(d)
    for i in range(2,20):
        for j in range(i+1,40):
             if y[i:j]==y[(j+1):(j+1)+(j-i)]:
                list1.append(d)
                list2.append(j-i)
            

    d = d+1

#    print(d)


print(list1)
print(list2)
