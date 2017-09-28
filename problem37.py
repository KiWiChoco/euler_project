from sympy import sieve

primes = []
quotient_list = []
remainder_list = []
sym_prime = []


def prime_generator(c,k): #소수 생성기
    for i in sieve.primerange(c, k) :
        primes.append(i)
    #print(primes)


# def is_prime(num): #소수 판별기 <--is_prime함수는 필요가없었음 소수리스트에서 판별하자
#     """Returns True if the number is prime
#     else False."""
#     if num == 0 or num == 1:
#         return False
#     for x in range(2, num):
#         if num % x == 0:
#             return False
#     else:
#         return True


def quotient(a): #뒤에서부터 하나씩 뺀 (== 몫인) 리스트를 만드는 함수

    length = len(str(a))
    for i in range(0,length,1):
        quotient_list.append(a//10**i)
    #print(quotient_list)
    #return quotient_list


def remainder(a): #앞에서부터 하나씩 뺀 (== 나머지인) 리스트를 만드는 함수
    # remainder_list = []
    remainder_list.append(a)
    length = len(str(a))
    for i in range(1,length,1):
        remainder_list.append(a%(10**i))
    #print(remainder_list)
    #return remainder_list


def sym(a):
    quotient_bool = []
    remainder_bool = []
    bool = []
    quotient(a)
    remainder(a)
    for i in range(len(quotient_list)):
        if quotient_list[i] in primes:   #<-왼쪽 오른쪽으로 자른 소수 리스트도 모두 소수라면 기본primes로 정의한 소수리스트에 들어가있을것 is_prime을 쓰지않게된 이유
            if remainder_list[i] in primes:
                bool.append(True)
            else : break
        else : break
    if len(bool) == len(quotient_list):
        sym_prime.append(a)


prime_generator(1,1000000)
for item in primes:
    sym(item)
    quotient_list = []
    remainder_list = []
    if len(sym_prime) == 15 : break #내가 짠 코드는 1부터 소수를 생성했다. sym에서 소수 리스트로 판단하기 위해서! 따라서 총 15개가 나오게된다
print(sym_prime) #총 15개가 나오지만 문제에서는 2,3,5,7을 빼고 더하라고했다 빼고 더하기만 하면 끝!! 결과는 잘 나온다 오래걸렸다.
