from sympy import sieve

primes = []

uni_primes = []

for i in sieve.primerange(2,100):
    primes.append(i)

for i in range(1,len(primes)):
    if primes[i] == sum(primes[:i-1]):
        uni_primes.append(i)

print(uni_primes[-1])