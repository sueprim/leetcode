class Solution:
    def countPrimes(self, n: int) -> int:
        primes = set(range(2, n))
        for num in range(2, int(n**0.5) + 1):
            if num in primes:
                for composite in range(num * 2, n, num):
                    primes.discard(composite)
        return len(primes)
