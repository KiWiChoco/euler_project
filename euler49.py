# a = set(list(range(1000,10000,1)))

from sympy import sieve

primes = []

for i in sieve.primerange(1000,10000):
    primes.append(i)

# print(primes)

primes_set = set(primes)

for i in primes_set:
    for j in primes_set:
        for k in primes_set:
            if (i!=j) and (i!=k) and (j!=k) and (j-i == k-j) :
                if (set(list(str(i))) == set(list(str(j)))) and ((set(list(str(j)))) == set(list(str(k)))) and (set(list(str(i))) == set(list(str(k)))):
                    print(i,j,k)
                    break
                else: continue
            else: continue

