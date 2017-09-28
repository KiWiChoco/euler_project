from sympy import sieve

primes = []
quotient_list = []
remainder_list = []
sym_prime = []


def prime_generator(c,k): #소수 생성기
    for i in sieve.primerange(c, k) :
        primes.append(i)
    #print(primes)


def is_prime(num): #소수 판별기
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


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
        if quotient_list[i] in primes:
            if remainder_list[i] in primes:
                bool.append(True)
            else : break
        else : break
    #         quotient_bool.append(True)
    #     else : break
    #
    #     if is_prime(remainder_list[i]):
    #         remainder_bool.append(True)
    #     else : break
    #
    # if (len(quotient_bool) == len(quotient_list)) and (len(remainder_bool) == len(remainder_list)):
    #     sym_prime.append(a)
    if len(bool) == len(quotient_list):
        sym_prime.append(a)



prime_generator(1,1000000)
for item in primes:
    sym(item)
    quotient_list = []
    remainder_list = []
print(sym_prime)
