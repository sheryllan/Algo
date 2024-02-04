"""
You are climbing a staircase. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to
the top?
"""
from functools import reduce
import math

# f(n) = sum(C(n-i)^i), where i ranging from 0 to m = n // 2, is the sum of all combination of choosing i from n-i
def climbing_steps(n):
    count = 1
    m = n // 2
    for i in range(1, m + 1):
        numerator = reduce(lambda x, y: x * y, (z for z in range(n - 2 * i + 1, n - i + 1)))
        denominator = reduce(lambda x, y: x * y, (z for z in range(1, i + 1)))
        count += numerator / denominator

    return count


# Fibonacci solution
def climbing_steps_dp(n):
    f1 = f2 = 1
    for i in range(2, n+1):
        temp = f2
        f2 += f1
        f1 = temp
    return f2


for i in range(100):
    r1 = climbing_steps(i)
    r2 = climbing_steps_dp(i)
    assert math.isclose(r1, r1), f'{i}: {r1}!= {r2}'
    # print(f'{climbing_steps(i)} vs {climbing_steps_dp(i)}')