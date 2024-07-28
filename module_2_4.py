numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for primes in range(1, len(numbers) + 1):
    if primes > 1:
       for i in range(2, primes):
           if (primes % i) == 0:
               break
       else:
           print("ПРОСТОЕ ЧИСЛО ", primes)

for not_primes in range(1, len(numbers) + 1):
    if not_primes > 1:
       for i in range(2, not_primes):
           if ((not_primes % i) > 0) :
               break
           else:
               print("НЕ СОСТАВНОЕ ЧИСЛО", not_primes)