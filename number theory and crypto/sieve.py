def sieve_of_eratosthenes(n,start=2):
    """
    Returns all prime numbers up to n using the Sieve of Eratosthenes.
    """
    primes = [True] * n
    primes[0] = primes[1] = False
    list_of_primes = []
    for i, is_prime in enumerate(primes):
        if is_prime:
        
            for j in range(i * i, n, i):
                primes[j] = False
    
    for i, is_prime in enumerate(primes):
        if is_prime:
            list_of_primes.append(i)
    return list_of_primes


print(sieve_of_eratosthenes(10000))