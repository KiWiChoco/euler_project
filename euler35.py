from sympy import sieve

primes_list = []

circul_num = set()

for i in sieve.primerange(2,1000000):
    primes_list.append(i)

primes = set(primes_list)


def circul(prime_num):
    if len(str(prime_num)) == 1:
        circul_num.add(prime_num)

    else:
        length = len(str(prime_num))
        str_prime = str(prime_num)
        cir_set = set()
        for i in range(1,length):
            cir_set.add(str_prime[i:]+str_prime[:i])

        cir_bool = set()
        for j in cir_set:
            #print(j)
            if int(j) in primes:
                cir_bool.add(True)
            else: cir_bool.add(False)
        #print(cir_bool)
        if False not in cir_bool:
            circul_num.add(prime_num)


for i in primes:
    circul(i)
print(len(circul_num))
