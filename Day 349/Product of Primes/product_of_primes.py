class Solution:
    def primeProduct(self, L, R):
        MOD = 10**9 + 7

        def sieve(limit):
            is_prime = [True] * (limit + 1)
            p = 2
            primes = []
            while p * p <= limit:
                if is_prime[p]:
                    for i in range(p * p, limit + 1, p):
                        is_prime[i] = False
                p += 1
            for p in range(2, limit + 1):
                if is_prime[p]:
                    primes.append(p)
            return primes

        limit = int(R**0.5) + 1
        base_primes = sieve(limit)

        is_prime_in_range = [True] * (R - L + 1)
        for prime in base_primes:
            start = max(prime * prime, L + (prime - L % prime) % prime)
            for j in range(start, R + 1, prime):
                is_prime_in_range[j - L] = False

        if L == 1:
            is_prime_in_range[0] = False

        product = 1
        found_prime = False
        for i in range(R - L + 1):
            if is_prime_in_range[i]:
                product = (product * (L + i)) % MOD
                found_prime = True

        return product if found_prime else 1