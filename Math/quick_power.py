
def quick_power(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x

        x = x * x
        n = n // 2

    return result


print(quick_power(2, 10))
print(quick_power(3, 5))
print(quick_power(2, 1))