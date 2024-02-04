"""
A cybersecurity firm has discovered a new type of encryption being used by a group of hackers.
The encryption key will be a valid kev. which is a number that has exactly 3 factors or divisors.

For example, 4 is a valid key because it has exactly 3 factors: 1, 2, and 4.
But 6 is not a valid key because it has 4 factors: 1, 2, 3, and 6.

Given an array keys of length n, find the number of valid keys in the range [1, keys[i]], both inclusive for earn o<i<n

NOTE:
    a is called a divisor of b is there is an integer c such that c * a = b
    only positive integers are considered for counting divisors


Example:
    n = 2, keys = [5, 11]
    key[i]  valid keys
    key[0]   4
    key[1]   4, 9

    Hence, the answer is [1,2]
"""
import math


def get_divisor_counts(N: int):
    if N < 2:
        return [0] * N

    # 0 to indicate the number is a prime number
    divisor_cnt = [0] * (N + 1)

    for x in range(2, N + 1):
        if divisor_cnt[x] != 0:
            continue

        start = x * x
        for i in range(start, N + 1, x):
            divisor_cnt[i] += 1 if i == start else 2

    return divisor_cnt


def get_valid_key_count(keys):
    N = max(keys)
    counts = get_divisor_counts(N)

    valid_keys = [0] * len(counts)
    valid_keys_so_far = 0
    for i in range(len(counts)):
        if counts[i] == 1:
            valid_keys_so_far += 1
        valid_keys[i] = valid_keys_so_far
    return [valid_keys[k] for k in keys]


def get_prime_flags(N: int):
    is_prime = [1] * (N + 1)
    is_prime[0] = is_prime[1] = 0
    for x in range(2, N + 1):
        if not is_prime[x]:
            continue

        start = x * x
        for i in range(start, N + 1, x):
            is_prime[i] = 0

    return is_prime


def get_valid_key_count2(keys):
    N = max(keys)
    primes = get_prime_flags(N)
    prime_count_so_far = 0
    for i in range(len(primes)):
        prime_count_so_far += primes[i]
        primes[i] = prime_count_so_far

    return [primes[int(math.sqrt(k))] for k in keys]



if __name__ == '__main__':
    # counts = get_divisor_counts(50)
    # print({i: counts[i] for i in range(len(counts))})
    print(get_valid_key_count2([5, 100, 11, 9, 40, 50]))
