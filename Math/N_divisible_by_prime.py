# Sieve of Eratosthenes
def get_primes(N: int):
    if N < 2:
       return

    is_prime = [True] * (N + 1)
    for x in range(2, N + 1):
        if is_prime[x]:
            yield x

        for i in range(x * x, N + 1, x):
            is_prime[i] = False



# p = list(get_primes(30))
# print(p)



def get_nums_primes_divisible(p, q, N):
    mutiple = p * q
    for i in range(mutiple, N + 1, mutiple):
        yield i


# 1D dp solution with time complexity O(N*k), where k is the number of primes within N
def get_count_nums_primes_divisible(N):
    count = 0
    marked = [0] * (N + 1)
    for p in get_primes(N // 2):
        for x in range(p, N + 1, p):
            count += marked[x]
            marked[x] += 1

    return count


# def test(N):
#     count = 0
#     primes = list(get_primes(N))
#     n_primes = len(primes)
#     for i in range(0, n_primes - 1):
#         for j in range(i + 1, n_primes):
#             for _ in get_nums_primes_divisible(primes[i], primes[j], N):
#                 count += 1
#
#     return count


# print(test(10000))


# print(get_count_nums_primes_divisible(10000))
print(get_count_nums_primes_divisible(20))
print(get_count_nums_primes_divisible(1000000))

