# prime_numbers.py

def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    """Return a list of prime numbers up to the given limit."""
    primes = [n for n in range(2, limit + 1) if is_prime(n)]
    return primes
