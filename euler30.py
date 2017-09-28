#euler 30

def euler30_sum(li):
    sum=0
    for i in range(len(li)):
        sum=sum+(li[i]**5)
    return sum
        

def digit(n,a):
    return (n//10**(a-1))%10


def li_t(n):
    li=[]
    for i in range(1,len(str(n))+1):
        li.append(digit(n,i))
    return li

def euler30():
    n_list=[]
    n=2
    while n<10000000:
        #li=[]
        #for i in range(1,len(str(n))+1):
            #li.append(digit(n,i))
            #if n==euler30_sum(li):
                #print(n)
        if n==euler30_sum(li_t(n)):
            print(n)
            n_list.append(n)
            

        n+=1

    print('sum of n_list :',sum(n_list))

euler30()


