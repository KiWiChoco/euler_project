#euler 34


def digits(n,a): #각 자리수를 추출하는 def 1234라면 1,2,3,4 를 추출 a=1,2,3,4에따라
    return (n//10**(a-1))%10


def sum_factorial(li): # 추출한 자릿수를 li_test에서 리스트로 만들어서 펙토리얼합을 구해줄함수
    import math
    sum=0
    for i in range(len(li)):
        sum = sum + math.factorial(li[i])
    return sum

def li_test(n): #digits함수에서 추출한 각 자릿수를 리스트로 저장해줄 함수
    li=[]
    for i in range(1,len(str(n))+1):
        li.append(digits(n,i))
    return li


def euler34(): #최종함수 

    n=3
    result_li=[]    
    while n<100000:
        if n==sum_factorial(li_test(n)):
            result_li.append(n)

        n+=1

    print(result_li)

    print('sum of result_li is :',sum(result_li))

